class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        queue = deque([[m, n]])

        while queue:
            x, y = queue.popleft()
            if x < 0 or y < 0:
                continue
            if dp[x][y] == float('inf'):
                if x == m and y == n:
                    dp[x][y] = 0
                elif x == m:
                    dp[m][y] = n-y
                elif y == n:
                    dp[x][n] = m-x
                else:
                    if word1[x] == word2[y]:
                        dp[x][y] = dp[x+1][y+1]
                    else:
                        dp[x][y] = 1 + min(dp[x+1][y], dp[x][y+1], dp[x+1][y+1])
                queue.append([x-1, y])
                queue.append([x, y-1])
        
        return dp[0][0]