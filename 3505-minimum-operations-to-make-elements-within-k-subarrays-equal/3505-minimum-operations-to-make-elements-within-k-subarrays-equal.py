
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit_mask >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        count = Fenwick(m)
        sums = Fenwick(m)

        total = 0
        costs = []

        def add(v, delta):
            nonlocal total
            r = rank[v]
            count.update(r, delta)
            sums.update(r, v * delta)
            total += v * delta

        def get_cost():
            median_rank = count.kth((x + 1) // 2)
            median = vals[median_rank - 1]

            left_count = count.query(median_rank)
            left_sum = sums.query(median_rank)

            right_count = x - left_count
            right_sum = total - left_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        # Initial window
        for i in range(x):
            add(nums[i], 1)

        costs.append(get_cost())

        # Sliding window
        for i in range(x, n):
            add(nums[i - x], -1)
            add(nums[i], 1)
            costs.append(get_cost())

        # DP: previous and current rows
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x and prev[i - x] != INF:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
