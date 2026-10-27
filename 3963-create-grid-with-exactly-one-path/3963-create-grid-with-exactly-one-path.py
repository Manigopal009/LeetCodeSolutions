class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Fill the grid with obstacles ('#')
        grid = [["#" for _ in range(n)] for _ in range(m)]
        
        # Create a single valid path going right along the first row, then down along the last column
        for j in range(n):
            grid[0][j] = "."
        for i in range(1, m):
            grid[i][n - 1] = "."
            
        return ["".join(row) for row in grid]