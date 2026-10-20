class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            prev_max = None
            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]

                descents = sum(
                    block[i] > block[(i + 1) % k]
                    for i in range(k)
                )

                if descents > 1:
                    valid = False
                    break

                if prev_max is not None and prev_max > min(block):
                    valid = False
                    break

                prev_max = max(block)

            if valid:
                ans += k

        return ans