class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        max_len = 1
        start = 0

        for i in range(n):
            dp[i][i] = 1
            for j in range(i):
                l = i - j + 1
                if s[i] == s[j] and (l < 4 or dp[j+1][i-1]):
                    dp[j][i] = True
                    
                    if max_len < l:
                        max_len = l
                        start = j
        
        return s[start:start+max_len]