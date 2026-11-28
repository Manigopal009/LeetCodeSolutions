from collections import defaultdict
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        if not items or budget <= 0:
            return 0

        max_factor = max(factor for factor, _ in items)
        min_price = min(price for _, price in items)

        # Count how many items exist for each factor value
        factor_count = [0] * (max_factor + 1)
        for factor, _ in items:
            factor_count[factor] += 1

        # For each factor d, sum counts of multiples of d (including d itself)
        multiples_count = [0] * (max_factor + 1)
        for d in range(1, max_factor + 1):
            if factor_count[d] == 0:
                continue
            total_mult = 0
            for m in range(d, max_factor + 1, d):
                total_mult += factor_count[m]
            multiples_count[d] = total_mult

        # Aggregate how many value-2 copies are available at each price
        # (subtract 1 to exclude the item itself, since i != j)
        units_by_price = defaultdict(int)
        for factor, price in items:
            gain = multiples_count[factor] - 1
            if gain > 0 and price <= 2 * min_price:
                units_by_price[price] += gain

        total_items = 0
        rem_budget = budget

        # Greedily buy value-2 marginal units from cheapest price upward
        for price in sorted(units_by_price):
            available = units_by_price[price]
            buy = min(available, rem_budget // price)
            if buy > 0:
                total_items += 2 * buy
                rem_budget -= buy * price

        # Spend remaining budget on the cheapest item (value 1 each)
        total_items += rem_budget // min_price
        return total_items