class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        
        # Count the frequency of set bits at each position
        for x in nums:
            for i in range(31):
                if (x >> i) & 1:
                    bit_counts[i] += 1
        
        # Construct the k largest possible numbers
        max_nums = [0] * k
        for i in range(31):
            # Distribute the bits to the top k numbers
            for j in range(k):
                if bit_counts[i] > 0:
                    max_nums[j] |= (1 << i)
                    bit_counts[i] -= 1
        
        # Calculate the sum of squares modulo 10^9 + 7
        total_sum = 0
        for x in max_nums:
            total_sum = (total_sum + (x * x) % MOD) % MOD
            
        return total_sum