class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = 1

        for x in nums:
            # Use x -> x + 1 (extends consecutive chain ending at x)
            dp[x + 1] = dp.get(x, 0) + 1
            # Use x -> x (extends consecutive chain ending at x - 1)
            dp[x] = dp.get(x - 1, 0) + 1

            ans = max(ans, dp[x + 1], dp[x])

        return ans