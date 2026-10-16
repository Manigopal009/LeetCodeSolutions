class SegmentTreeNode:
    def __init__(self):
        self.sum_val = 0
        self.count = 0
        self.lazy = 0

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment tree arrays (4 * N size)
        tree_sum = [0] * (4 * n)
        tree_count = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push_down(node, l, r):
            if lazy[node] != 0:
                mid = (l + r) // 2
                val = lazy[node]
                
                # Left child update
                left = 2 * node
                tree_sum[left] = (tree_sum[left] + 2 * val * tree_count[left] + val * val * (mid - l + 1)) % MOD
                tree_count[left] = (tree_count[left] + val * (mid - l + 1)) % MOD
                lazy[left] = (lazy[left] + val) % MOD
                
                # Right child update
                right = 2 * node + 1
                tree_sum[right] = (tree_sum[right] + 2 * val * tree_count[right] + val * val * (r - mid)) % MOD
                tree_count[right] = (tree_count[right] + val * (r - mid)) % MOD
                lazy[right] = (lazy[right] + val) % MOD
                
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                tree_sum[node] = (tree_sum[node] + 2 * val * tree_count[node] + val * val * (r - l + 1)) % MOD
                tree_count[node] = (tree_count[node] + val * (r - l + 1)) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr, val)
                
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_count[node] = (tree_count[2 * node] + tree_count[2 * node + 1]) % MOD

        last_occurrence = {}
        total_sum = 0
        current_sum = 0
        
        for i, x in enumerate(nums):
            prev_idx = last_occurrence.get(x, -1)
            last_occurrence[x] = i
            
            # Update range [prev_idx + 1, i] with increment +1
            update(1, 0, n - 1, prev_idx + 1, i, 1)
            
            # tree_sum[1] now holds the sum of squares of all subarrays ending at i
            total_sum = (total_sum + tree_sum[1]) % MOD
            
        return total_sum