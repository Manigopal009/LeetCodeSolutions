import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Min-heap for available servers: stores (weight, index)
        available = []
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))
            
        # Min-heap for unavailable servers: stores (free_time, weight, index)
        unavailable = []
        
        ans = []
        curr_time = 0
        
        for j, task_time in enumerate(tasks):
            # Time cannot be behind the current task arrival time
            curr_time = max(curr_time, j)
            
            # If no servers are available at all, fast-forward time to the next server release
            if not available and unavailable[0][0] > curr_time:
                curr_time = unavailable[0][0]
                
            # Free up all servers whose tasks are completed by curr_time
            while unavailable and unavailable[0][0] <= curr_time:
                free_time, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
                
            # Assign the current task to the top server from the available heap
            weight, index = heapq.heappop(available)
            ans.append(index)
            
            # Push the server into the unavailable heap with its new release time
            heapq.heappush(unavailable, (curr_time + task_time, weight, index))
            
        return ans