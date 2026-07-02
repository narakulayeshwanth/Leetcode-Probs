from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])

        INF = 10**9
        dist = [[INF] * n for _ in range(m)]

        dist[0][0] = grid[0][0]
        dq = deque([(0, 0)])

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while dq:
            x, y = dq.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    w = grid[nx][ny]
                    nd = dist[x][y] + w

                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if w == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        return dist[m - 1][n - 1] < health