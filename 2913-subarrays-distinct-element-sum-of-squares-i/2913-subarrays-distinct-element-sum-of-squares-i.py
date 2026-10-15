class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        
        # Generate all possible subarrays
        for i in range(n):
            distinct_elements = set()
            for j in range(i, n):
                # Add current element to the set for the subarray nums[i..j]
                distinct_elements.add(nums[j])
                
                # Add the square of the count of distinct elements
                count = len(distinct_elements)
                total_sum += count * count
                
        return total_sum