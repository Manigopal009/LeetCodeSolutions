class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Ways to interleave left and right subtrees: C(len(left) + len(right), len(left))
            ways = math.comb(len(left) + len(right), len(left))
            
            # Multiply by the number of valid reorderings for left and right subtrees
            return (ways * helper(left) * helper(right)) % MOD

        import math
        return (helper(nums) - 1) % MOD