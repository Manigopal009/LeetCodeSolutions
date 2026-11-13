
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        LOG = n.bit_length()

        # 1. Next Greater Element
        ng = [n] * n
        st = []

        for i, x in enumerate(nums):
            while st and nums[st[-1]] < x:
                ng[st.pop()] = i
            st.append(i)

        # 2. Binary lifting
        jump = [ng]
        weight = [[nums[i] * (ng[i] - i) for i in range(n)]]

        for p in range(1, LOG):
            prev_j = jump[-1]
            prev_w = weight[-1]

            curr_j = [n] * n
            curr_w = [0] * n

            for i in range(n):
                mid = prev_j[i]

                if mid < n:
                    curr_j[i] = prev_j[mid]
                    curr_w[i] = prev_w[i] + prev_w[mid]
                else:
                    curr_w[i] = prev_w[i]

            jump.append(curr_j)
            weight.append(curr_w)

        # 3. Prefix sum
        pref = [0] * (n + 1)

        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x

        # 4. Calculate cost
        def getCost(l, r):
            total = 0
            cur = l

            for p in range(LOG - 1, -1, -1):
                nxt = jump[p][cur]

                if nxt <= r:
                    total += weight[p][cur]
                    cur = nxt

            total += nums[cur] * (r - cur + 1)

            return total - (pref[r + 1] - pref[l])

        # 5. Two pointers (instead of binary search)
        ans = 0
        left = 0

        for right in range(n):

            while left <= right and getCost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans
