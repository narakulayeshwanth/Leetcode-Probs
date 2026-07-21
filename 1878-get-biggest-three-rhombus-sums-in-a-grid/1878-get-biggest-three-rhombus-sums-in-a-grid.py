class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        vals = set()

        for i in range(m):
            for j in range(n):
                vals.add(grid[i][j])  # radius 0

                r = 1
                while (
                    i - r >= 0 and
                    i + r < m and
                    j - r >= 0 and
                    j + r < n
                ):
                    total = 0

                    # top -> right
                    for t in range(r):
                        total += grid[i - r + t][j + t]

                    # right -> bottom
                    for t in range(r):
                        total += grid[i + t][j + r - t]

                    # bottom -> left
                    for t in range(r):
                        total += grid[i + r - t][j - t]

                    # left -> top
                    for t in range(r):
                        total += grid[i - t][j - r + t]

                    vals.add(total)
                    r += 1

        return sorted(vals, reverse=True)[:3]