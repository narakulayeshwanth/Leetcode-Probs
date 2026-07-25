from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345

        n, m = len(grid), len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)

        N = len(arr)

        prefix = [1] * N
        for i in range(1, N):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD

        suffix = [1] * N
        for i in range(N - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD

        ans = [[0] * m for _ in range(n)]

        k = 0
        for i in range(n):
            for j in range(m):
                ans[i][j] = (prefix[k] * suffix[k]) % MOD
                k += 1

        return ans