from collections import deque
from sortedcontainers import SortedSet

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        cnt0 = s.count('0')

        even = SortedSet()
        odd = SortedSet()

        for i in range(n + 1):
            if i & 1:
                odd.add(i)
            else:
                even.add(i)

        if cnt0 & 1:
            odd.remove(cnt0)
        else:
            even.remove(cnt0)

        q = deque([cnt0])
        steps = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                if cur == 0:
                    return steps

                lo = cur + k - 2 * min(cur, k)
                hi = cur + k - 2 * max(0, k - (n - cur))

                st = even if lo % 2 == 0 else odd

                idx = st.bisect_left(lo)
                while idx < len(st) and st[idx] <= hi:
                    nxt = st[idx]
                    q.append(nxt)
                    st.remove(nxt)

            steps += 1

        return -1