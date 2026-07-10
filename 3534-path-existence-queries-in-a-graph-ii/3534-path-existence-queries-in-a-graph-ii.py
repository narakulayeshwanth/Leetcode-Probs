from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted((v, i) for i, v in enumerate(nums))
        vals = [v for v, _ in order]

        pos = [0] * n
        comp = [0] * n

        cid = 0
        for i, (_, idx) in enumerate(order):
            pos[idx] = i
            if i > 0 and vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[idx] = cid

        right = [0] * n
        for i in range(n):
            right[i] = bisect_right(vals, vals[i] + maxDiff) - 1

        left = [0] * n
        for i in range(n):
            left[i] = bisect_left(vals, vals[i] - maxDiff)

        LOG = n.bit_length()

        upR = [right]
        for _ in range(1, LOG):
            prev = upR[-1]
            upR.append([prev[prev[i]] for i in range(n)])

        upL = [left]
        for _ in range(1, LOG):
            prev = upL[-1]
            upL.append([prev[prev[i]] for i in range(n)])

        def forward(a, b):
            if a == b:
                return 0
            ans = 0
            cur = a
            for k in range(LOG - 1, -1, -1):
                if upR[k][cur] < b:
                    cur = upR[k][cur]
                    ans += 1 << k
            return ans + 1

        def backward(a, b):
            if a == b:
                return 0
            ans = 0
            cur = a
            for k in range(LOG - 1, -1, -1):
                if upL[k][cur] > b:
                    cur = upL[k][cur]
                    ans += 1 << k
            return ans + 1

        res = []
        for u, v in queries:
            if comp[u] != comp[v]:
                res.append(-1)
                continue
            pu, pv = pos[u], pos[v]
            if pu <= pv:
                res.append(forward(pu, pv))
            else:
                res.append(backward(pu, pv))
        return res