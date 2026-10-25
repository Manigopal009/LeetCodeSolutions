class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # If out of bounds, it's not a closed island (though border check handles outer limits)
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            # If it's water (1) or already visited, return
            if grid[r][c] == 1:
                return
            
            # Mark the current cell as visited by turning it into water (1)
            grid[r][c] = 1
            
            # Traverse all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Eliminate all 0s connected to the top and bottom borders
        for c in range(cols):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[rows - 1][c] == 0:
                dfs(rows - 1, c)
                
        # Step 2: Eliminate all 0s connected to the left and right borders
        for r in range(rows):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][cols - 1] == 0:
                dfs(r, cols - 1)
                
        # Step 3: Count remaining closed islands in the interior
        closed_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    closed_count += 1
                    dfs(r, c)
                    
        return closed_count