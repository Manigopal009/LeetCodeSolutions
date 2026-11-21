from typing import List


class Solution:

  def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    n = len(parent)

    # 1. Build initial adjacency list
    orig_adj: List[List[int]] = [[] for _ in range(n)]
    for i in range(1, n):
      orig_adj[parent[i]].append(i)

    new_parent = parent[:]
    last_seen = [-1] * 26

    # 2. DFS on original tree to find closest ancestor y with s[y] == s[x]
    def dfs_reassign(u: int) -> None:
      idx = ord(s[u]) - ord("a")
      prev_node = last_seen[idx]

      if u != 0 and prev_node != -1:
        new_parent[u] = prev_node

      last_seen[idx] = u
      for v in orig_adj[u]:
        dfs_reassign(v)
      last_seen[idx] = prev_node

    dfs_reassign(0)

    # 3. Build final tree adjacency list
    final_adj: List[List[int]] = [[] for _ in range(n)]
    for i in range(1, n):
      final_adj[new_parent[i]].append(i)

    ans = [1] * n

    # 4. DFS on final tree to calculate subtree sizes
    def dfs_size(u: int) -> int:
      size = 1
      for v in final_adj[u]:
        size += dfs_size(v)
      ans[u] = size
      return size

    dfs_size(0)
    return ans