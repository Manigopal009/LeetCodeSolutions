import bisect
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy_servers = []  # Min-heap storing (free_time, server_id)
        available = list(range(k))  # Sorted list of available server IDs
        request_count = [0] * k

        for i, (arr, ld) in enumerate(zip(arrival, load)):
            # 1. Free up servers whose tasks have finished by time 'arr'
            while busy_servers and busy_servers[0][0] <= arr:
                _, server_id = heapq.heappop(busy_servers)
                # Insert back into the sorted available list
                idx = bisect.bisect_left(available, server_id)
                available.insert(idx, server_id)

            # 2. If no servers are available, the request is dropped
            if not available:
                continue

            # 3. Find the first available server >= (i % k)
            target = i % k
            idx = bisect.bisect_left(available, target)

            # If no server >= target is available, wrap around to the beginning (index 0)
            if idx == len(available):
                idx = 0

            server_id = available.pop(idx)

            # 4. Assign the request to this server
            request_count[server_id] += 1
            heapq.heappush(busy_servers, (arr + ld, server_id))

        # 5. Find the maximum requests handled and return all servers with that count
        max_handled = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_handled]