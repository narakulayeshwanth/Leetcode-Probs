from collections import defaultdict

class Solution:
    def minScore(self, n, roads):
        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        visited = set()
        ans = float('inf')

        def dfs(node):
            nonlocal ans
            visited.add(node)

            for nei, d in graph[node]:
                ans = min(ans, d)
                if nei not in visited:
                    dfs(nei)

        dfs(1)
        return ans