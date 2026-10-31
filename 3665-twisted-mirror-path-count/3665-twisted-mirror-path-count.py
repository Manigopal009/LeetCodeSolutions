class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        right[0][0] = 1

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    pass

                # Process paths entering from the left
                if right[i][j]:
                    if grid[i][j] == 1:
                        if i + 1 < m:
                            down[i + 1][j] = (
                                down[i + 1][j] + right[i][j]
                            ) % MOD
                    else:
                        if j + 1 < n:
                            right[i][j + 1] = (
                                right[i][j + 1] + right[i][j]
                            ) % MOD

                        if i + 1 < m:
                            down[i + 1][j] = (
                                down[i + 1][j] + right[i][j]
                            ) % MOD

                # Process paths entering from above
                if down[i][j]:
                    if grid[i][j] == 1:
                        if j + 1 < n:
                            right[i][j + 1] = (
                                right[i][j + 1] + down[i][j]
                            ) % MOD
                    else:
                        if j + 1 < n:
                            right[i][j + 1] = (
                                right[i][j + 1] + down[i][j]
                            ) % MOD

                        if i + 1 < m:
                            down[i + 1][j] = (
                                down[i + 1][j] + down[i][j]
                            ) % MOD

        return (right[m - 1][n - 1] + down[m - 1][n - 1]) % MOD