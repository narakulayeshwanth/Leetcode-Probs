class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1

                target = 0
                ok = True

                for f in freq:
                    if f:
                        if target == 0:
                            target = f
                        elif f != target:
                            ok = False
                            break

                if ok:
                    ans = max(ans, j - i + 1)

        return ans