class Solution:
    def minOperations(self, s: str) -> int:
        # Case 0: Already sorted
        if list(s) == sorted(s):
            return 0
        
        n = len(s)
        
        # Case -1: Impossible to sort proper substrings of length <= 1
        if n == 2:
            return -1
        
        min_char = min(s)
        max_char = max(s)
        
        # Case 1: Minimum character is at index 0 or Maximum character is at index n-1
        if s[0] == min_char or s[-1] == max_char:
            return 1
        
        # Case 3: Only maximum character is at s[0] AND only minimum character is at s[-1]
        if s[0] == max_char and s[-1] == min_char and s.count(max_char) == 1 and s.count(min_char) == 1:
            return 3
        
        # Case 2: All other cases
        return 2