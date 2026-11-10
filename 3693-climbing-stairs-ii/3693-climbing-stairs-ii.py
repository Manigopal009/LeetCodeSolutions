class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for j in range(1, n + 1):
            for k in range(1, 4):  # Jump sizes: 1, 2, 3
                if j - k >= 0:
                    jump_cost = costs[j - 1] + k * k
                    dp[j] = min(dp[j], dp[j - k] + jump_cost)
                    
        return dp[n]