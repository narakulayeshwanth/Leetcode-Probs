import heapq

class Solution:
    def minCost(self, n: int, edges):
        out_edges = [[] for _ in range(n)]
        in_edges = [[] for _ in range(n)]

        for u, v, w in edges:
            out_edges[u].append((v, w))
            in_edges[v].append((u, w))

        INF = 10**18
        dist = [[INF] * 2 for _ in range(n)]

        dist[0][0] = 0
        pq = [(0, 0, 0)]  

        while pq:
            d, u, state = heapq.heappop(pq)

            if d != dist[u][state]:
                continue

            if u == n - 1:
                return d

            for v, w in out_edges[u]:
                nd = d + w

                if nd < dist[v][0]:
                    dist[v][0] = nd
                    heapq.heappush(pq, (nd, v, 0))

            if state == 0:
                for v, w in in_edges[u]:
                    nd = d + 2 * w

                    if nd < dist[v][0]:
                        dist[v][0] = nd
                        heapq.heappush(pq, (nd, v, 0))

        return -1