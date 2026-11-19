class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(
            nums[-3] - nums[0],  # change two largest elements
            nums[-1] - nums[2],  # change two smallest elements
            nums[-2] - nums[1],  # change one smallest and one largest
        )