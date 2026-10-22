class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        idx0 = nums.index(0)
        
        # Check if nums is cyclically increasing
        is_increasing = True
        for i in range(n - 1):
            if nums[(idx0 + i + 1) % n] != nums[(idx0 + i) % n] + 1:
                is_increasing = False
                break
                
        if is_increasing:
            # Option 1: Only left rotations
            cost1 = idx0
            # Option 2: Reverse, rotate left, reverse back
            cost2 = ((n - idx0) % n) + 2
            return min(cost1, cost2)
        
        # Check if nums is cyclically decreasing
        is_decreasing = True
        for i in range(n - 1):
            if nums[(idx0 - (i + 1)) % n] != nums[(idx0 - i) % n] + 1:
                is_decreasing = False
                break
                
        if is_decreasing:
            # Option 1: Reverse then rotate left
            cost1 = 1 + (n - 1 - idx0)
            # Option 2: Rotate left then reverse
            cost2 = ((idx0 + 1) % n) + 1
            return min(cost1, cost2)
        
        return -1