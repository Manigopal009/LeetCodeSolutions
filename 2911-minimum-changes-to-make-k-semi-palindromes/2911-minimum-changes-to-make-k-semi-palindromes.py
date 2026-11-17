class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')
        
        # Precompute proper divisors for every possible substring length up to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length // 2 + 1):
                if length % d == 0:
                    divisors[length].append(d)
        
        # Helper to find min changes to make s[i..j] a semi-palindrome
        def get_semi_palindrome_cost(i: int, j: int) -> int:
            length = j - i + 1
            min_changes = INF
            
            for d in divisors[length]:
                changes = 0
                # Check each of the d interleaved groups
                for offset in range(d):
                    left = i + offset
                    right = j - (d - 1 - offset)
                    while left < right:
                        if s[left] != s[right]:
                            changes += 1
                        left += d
                        right -= d
                min_changes = min(min_changes, changes)
                
            return min_changes

        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_semi_palindrome_cost(i, j)
                
        # dp[i][p] = min changes to partition s[0..i-1] into p semi-palindromes
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for parts in range(1, k + 1):
            # Each part needs at least 2 characters, so minimum index is 2 * parts
            for i in range(2 * parts, n + 1):
                for prev in range(2 * (parts - 1), i - 1):
                    if dp[prev][parts - 1] != INF:
                        dp[i][parts] = min(
                            dp[i][parts], 
                            dp[prev][parts - 1] + cost[prev][i - 1]
                        )
                        
        return dp[n][k]