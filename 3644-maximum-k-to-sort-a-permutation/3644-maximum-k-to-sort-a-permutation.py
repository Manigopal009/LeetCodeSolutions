class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = None
        for i, val in enumerate(nums):
            if val != i:
                if ans is None:
                    ans = val
                else:
                    ans &= val
        
        return ans if ans is not None else 0