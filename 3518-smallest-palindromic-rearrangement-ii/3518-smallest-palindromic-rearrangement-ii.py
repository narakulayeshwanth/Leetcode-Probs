from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        cnt = [0] * 26
        mid = ""

        for i in range(26):
            ch = chr(ord('a') + i)
            cnt[i] = freq[ch] // 2
            if freq[ch] & 1:
                mid = ch

        LIMIT = 10 ** 6 + 1

        def ways(cnt):
            total = sum(cnt)
            ans = 1

            for x in cnt:
                if x:
                    ans *= comb(total, x)
                    if ans >= LIMIT:
                        return LIMIT
                    total -= x
            return ans

        if ways(cnt) < k:
            return ""

        left = []

        total = sum(cnt)

        while total:
            for c in range(26):
                if cnt[c] == 0:
                    continue

                cnt[c] -= 1
                w = ways(cnt)

                if w >= k:
                    left.append(chr(c + ord('a')))
                    total -= 1
                    break

                k -= w
                cnt[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]