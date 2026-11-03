class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_val = max(nums)
        return sum(max_val - num for num in nums)