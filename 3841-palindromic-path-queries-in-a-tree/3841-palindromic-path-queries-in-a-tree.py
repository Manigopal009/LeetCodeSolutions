class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Binary Lifting for LCA & Euler Tour
        LOG = 17
        up = [[-1] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        euler = []
        timer = 0
        
        def dfs(u, p, d):
            nonlocal timer
            tin[u] = timer
            euler.append(u)
            timer += 1
            depth[u] = d
            up[u][0] = p
            for i in range(1, LOG):
                if up[u][i - 1] != -1:
                    up[u][i] = up[up[u][i - 1]][i - 1]
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)
            tout[u] = timer - 1
            
        dfs(0, -1, 0)
        
        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[u] >= tout[v]
            
        def get_lca(u, v):
            if is_ancestor(u, v): return u
            if is_ancestor(v, u): return v
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != -1 and not is_ancestor(up[u][i], v):
                    u = up[u][i]
            return up[u][0]

        # Segment Tree over Euler Tour
        tree = [0] * (4 * n)
        node_val = [1 << (ord(ch) - ord('a')) for ch in s]
        
        def build(node, l, r):
            if l == r:
                tree[node] = node_val[euler[l]]
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            tree[node] = tree[2 * node] ^ tree[2 * node + 1]
            
        build(1, 0, n - 1)
        
        def update_tree(node, l, r, idx, val):
            if l == r:
                tree[node] = val
                return
            mid = (l + r) // 2
            if idx <= mid:
                update_tree(2 * node, l, mid, idx, val)
            else:
                update_tree(2 * node + 1, mid + 1, r, idx, val)
            tree[node] = tree[2 * node] ^ tree[2 * node + 1]
            
        def query_tree(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            return query_tree(2 * node, l, mid, ql, qr) ^ query_tree(2 * node + 1, mid + 1, r, ql, qr)

        def query_path(u, v):
            lca = get_lca(u, v)
            # Combine paths from u to lca and v to lca using Euler tour ranges
            # Since Euler tour stores subtrees, we can query subsegments or use heavy-light decomposition.
            # Alternatively, using prefix XOR from root if maintained:
            pass

        # For simplicity and correctness with standard path updates, HLD or path-decomposition via Euler ranges:
        # Since standard subtree range query covers subtrees, let's use node-to-root queries or HLD.
        # Below is an adapted path query using node-to-root prefix XORs maintained in Fenwick/Segment tree:
        
        # Let's use Fenwick tree on Euler tour tin indices for subtree/path queries:
        bit = [0] * (n + 1)
        def add(idx, val):
            idx += 1
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def pref(idx):
            idx += 1
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        # Initialize BIT with initial characters mapped to tin
        for i in range(n):
            add(tin[i], node_val[i])
            add(tout[i] + 1, node_val[i])

        results = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_val = 1 << (ord(c) - ord('a'))
                diff = node_val[u] ^ new_val
                node_val[u] = new_val
                add(tin[u], diff)
                add(tout[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                # Path XOR sum from u to v = pref(u) ^ pref(v) ^ node_val[lca]
                mask = pref(tin[u]) ^ pref(tin[v]) ^ node_val[lca]
                if (mask & (mask - 1)) == 0:
                    results.append(True)
                else:
                    results.append(False)
                    
        return results