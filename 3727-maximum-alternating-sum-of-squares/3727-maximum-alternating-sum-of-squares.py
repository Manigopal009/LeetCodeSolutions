class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Square each element and sort them
        squares = sorted([x * x for x in nums])
        n = len(squares)
        
        # Subtract the first half (smallest elements) and add the second half (largest elements)
        ans = 0
        for i in range(n):
            if i < n // 2:
                ans -= squares[i]
            else:
                ans += squares[i]
                
        return ans