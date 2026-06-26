from heapq import heappush, heappop
from bisect import bisect_right

class Solution:
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        N = m * n

        # id <-> cell
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))

        # Cells sorted by value
        order = sorted(range(N), key=lambda x: cells[x][0])
        sorted_vals = [cells[idx][0] for idx in order]
        pos_in_sorted = [0] * N
        for p, idx in enumerate(order):
            pos_in_sorted[idx] = p

        INF = 10 ** 18
        dist = [[INF] * N for _ in range(k + 1)]

        start = 0
        dist[0][start] = 0
        pq = [(0, 0, start)]  # (cost, teleports_used, cell_id)

        # DSU "next" arrays for each teleport layer
        parent = []
        for _ in range(k):
            parent.append(list(range(N + 1)))

        def find(layer, x):
            p = parent[layer]
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x

        while pq:
            d, t, u = heappop(pq)
            if d != dist[t][u]:
                continue

            _, x, y = cells[u]

            # Normal moves
            if y + 1 < n:
                v = u + 1
                nd = d + grid[x][y + 1]
                if nd < dist[t][v]:
                    dist[t][v] = nd
                    heappush(pq, (nd, t, v))

            if x + 1 < m:
                v = u + n
                nd = d + grid[x + 1][y]
                if nd < dist[t][v]:
                    dist[t][v] = nd
                    heappush(pq, (nd, t, v))

            # Teleport
            if t < k:
                limit = bisect_right(sorted_vals, cells[u][0]) - 1
                if limit >= 0:
                    idx = find(t, 0)
                    while idx <= limit:
                        cell = order[idx]
                        if d < dist[t + 1][cell]:
                            dist[t + 1][cell] = d
                            heappush(pq, (d, t + 1, cell))
                        parent[t][idx] = idx + 1
                        idx = find(t, idx)

        target = N - 1
        return min(dist[t][target] for t in range(k + 1))