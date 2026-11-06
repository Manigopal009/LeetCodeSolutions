class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda x: x[1])
        
        # Sort queries while keeping track of their original indices
        indexed_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        ans = [0] * len(queries)
        server_count = {}
        
        l = 0
        r = 0
        m = len(logs)
        
        for q_idx, q_time in indexed_queries:
            left_bound = q_time - x
            right_bound = q_time
            
            # Expand the window right pointer while log time <= right_bound
            while r < m and logs[r][1] <= right_bound:
                server_id = logs[r][0]
                server_count[server_id] = server_count.get(server_id, 0) + 1
                r += 1
                
            # Shrink the window left pointer while log time < left_bound
            while l < m and logs[l][1] < left_bound:
                server_id = logs[l][0]
                server_count[server_id] -= 1
                if server_count[server_id] == 0:
                    del server_count[server_id]
                l += 1
                
            # Total servers - servers that received at least one request in the window
            ans[q_idx] = n - len(server_count)
            
        return ans