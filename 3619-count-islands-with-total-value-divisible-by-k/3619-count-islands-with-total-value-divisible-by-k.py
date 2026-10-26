from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                total = 0
                stack = [(i, j, grid[i][j])]
                grid[i][j] = 0

                while stack:
                    r, c, value = stack.pop()
                    total += value

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                            value = grid[nr][nc]
                            grid[nr][nc] = 0
                            stack.append((nr, nc, value))

                if total % k == 0:
                    ans += 1

        return ans