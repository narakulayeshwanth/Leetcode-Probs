from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        NEG = -10**18
        dp = [[[NEG] * 3 for _ in range(n)] for _ in range(m)]

        # Initialize start cell
        if coins[0][0] >= 0:
            dp[0][0][0] = coins[0][0]
        else:
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                val = coins[i][j]

                for k in range(3):
                    best = NEG

                    if i > 0:
                        best = max(best, dp[i - 1][j][k])
                    if j > 0:
                        best = max(best, dp[i][j - 1][k])

                    if best != NEG:
                        dp[i][j][k] = max(dp[i][j][k], best + val)

                    if val < 0 and k > 0:
                        best = NEG
                        if i > 0:
                            best = max(best, dp[i - 1][j][k - 1])
                        if j > 0:
                            best = max(best, dp[i][j - 1][k - 1])

                        if best != NEG:
                            dp[i][j][k] = max(dp[i][j][k], best)

        return max(dp[m - 1][n - 1])