from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7

        pos = []
        dig = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                dig.append(int(ch))

        m = len(dig)

        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefVal = [0] * (m + 1)
        prefSum = [0] * (m + 1)

        for i in range(m):
            prefVal[i + 1] = (prefVal[i] * 10 + dig[i]) % MOD
            prefSum[i + 1] = prefSum[i] + dig[i]

        ans = []

        for l, r in queries:
            L = bisect_left(pos, l)
            R = bisect_right(pos, r) - 1

            if L > R:
                ans.append(0)
                continue

            length = R - L + 1

            x = (prefVal[R + 1] - prefVal[L] * pow10[length]) % MOD
            digit_sum = prefSum[R + 1] - prefSum[L]

            ans.append((x * digit_sum) % MOD)

        return ans