class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Number of units needed for both requirements simultaneously
        common = min(need1, need2)
        
        # Remaining needs after satisfying the common portion
        rem1 = need1 - common
        rem2 = need2 - common
        
        # Cost for the common part using the cheaper option between (costBoth) and (cost1 + cost2)
        total_cost = common * min(costBoth, cost1 + cost2)
        
        # Cost for the remaining type 1 requirement
        total_cost += rem1 * min(costBoth, cost1)
        
        # Cost for the remaining type 2 requirement
        total_cost += rem2 * min(costBoth, cost2)
        
        return total_cost