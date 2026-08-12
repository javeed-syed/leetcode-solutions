class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def solve(i, j, dp):
            curr = 1
            for x, y in [(0,1), (1,0), (0,-1), (-1, 0)]:
                ni = x + i
                nj = y + j

                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue
                
                if matrix[ni][nj] <= matrix[i][j]:
                    continue

                if dp[ni][nj] != -1:
                    curr = max(curr, 1 + dp[ni][nj])
                else:
                    curr = max(curr, 1 + solve(ni, nj, dp))
            
            dp[i][j] = curr
            return curr

        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1] * n for _ in range(m)]

        res = 1

        for i in range(m):
            for j in range(n):
                curr = solve(i, j, dp)
                res = max(curr, res)

        return res
    