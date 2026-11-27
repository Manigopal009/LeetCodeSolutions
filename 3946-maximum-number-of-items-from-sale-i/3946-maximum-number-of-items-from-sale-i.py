
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        max_factor = max(factor for factor, price in items)

        factor_freq = [0] * (max_factor + 1)

        for factor, price in items:
            factor_freq[factor] += 1

        multiples_count = [0] * (max_factor + 1)

        for f in range(1, max_factor + 1):
            for m in range(f, max_factor + 1, f):
                multiples_count[f] += factor_freq[m]

        dp = [0] * (budget + 1)

        for factor, price in items:

            if price <= 0:
                continue

            if price > budget:
                continue

            bonus = multiples_count[factor] - 1

            next_dp = dp[:]

            for r in range(min(price, budget + 1)):

                best = float('-inf')

                for b in range(r, budget + 1, price):

                    t = (b - r) // price

                    # Buy at least one copy
                    if t > 0:
                        candidate = t + bonus + best
                        next_dp[b] = max(next_dp[b], candidate)

                    # Prepare maximum for future budgets
                    best = max(best, dp[b] - t)

            dp = next_dp

        return max(dp)
