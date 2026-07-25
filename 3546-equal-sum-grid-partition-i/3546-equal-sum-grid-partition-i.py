from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = sum(sum(row) for row in grid)

        if total % 2:
            return False

        # Horizontal cuts
        curr = 0
        for i in range(m - 1):
            curr += sum(grid[i])
            if curr * 2 == total:
                return True

        # Column sums
        col = [0] * n
        for i in range(m):
            for j in range(n):
                col[j] += grid[i][j]

        # Vertical cuts
        curr = 0
        for j in range(n - 1):
            curr += col[j]
            if curr * 2 == total:
                return True

        return False