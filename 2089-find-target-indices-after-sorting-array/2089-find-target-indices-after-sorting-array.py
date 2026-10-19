class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count = nums.count(target)
        less = sum(1 for x in nums if x < target)
        return list(range(less, less + count))