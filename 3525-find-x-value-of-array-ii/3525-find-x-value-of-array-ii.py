from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # tree[node] = [product modulo k, counts of prefix products]
        tree = [[1 % k, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            lp, lc = left
            rp, rc = right

            prod = (lp * rp) % k
            cnt = lc[:]

            for r in range(k):
                cnt[(lp * r) % k] += rc[r]

            return [prod, cnt]

        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                tree[node] = [v, [0] * k]
                tree[node][1][v] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, pos, value):
            if l == r:
                v = value % k
                tree[node] = [v, [0] * k]
                tree[node][1][v] = 1
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2, l, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, r, pos, value)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            # This update persists for later queries
            update(1, 0, n - 1, index, value)

            # Remaining array is nums[start:]
            result = query(1, 0, n - 1, start, n - 1)

            ans.append(result[1][x])

        return ans