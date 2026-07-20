class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)

        k %= (m * n)
        arr = arr[-k:] + arr[:-k]

        ans = []
        idx = 0

        for _ in range(m):
            ans.append(arr[idx:idx + n])
            idx += n

        return ans