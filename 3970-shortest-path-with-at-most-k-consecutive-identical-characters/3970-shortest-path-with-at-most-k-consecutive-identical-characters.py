import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list: u -> list of (v, w)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Min-priority queue stores (distance, u, count)
        pq = []
        
        # Distance table: dist[u][count]
        # Since count ranges from 1 to k, we can use a dictionary or 2D array of size n x (k + 1)
        dist = {}
        
        # Start at node 0 with initial count 1 and distance 0
        initial_count = 1
        heapq.heappush(pq, (0, 0, initial_count))
        dist[(0, initial_count)] = 0
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            # If we reached the destination node, return the distance
            if u == n - 1:
                return d
                
            if d > dist.get((u, count), float('inf')):
                continue
                
            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                if next_count <= k:
                    next_d = d + w
                    if next_d < dist.get((v, next_count), float('inf')):
                        dist[(v, next_count)] = next_d
                        heapq.heappush(pq, (next_d, v, next_count))
                        
        return -1