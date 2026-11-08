class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        row_count = [0] * m
        col_count = [0] * n
        
        # First pass: record the number of servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
                    
        # Second pass: count servers that share a row or column with at least one other server
        communicating_servers = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        communicating_servers += 1
                        
        return communicating_servers