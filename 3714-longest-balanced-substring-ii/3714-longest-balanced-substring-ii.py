class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1

        run = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                run += 1
            else:
                run = 1
            ans = max(ans, run)

        pairs = [('a', 'b', 'c'),
                 ('a', 'c', 'b'),
                 ('b', 'c', 'a')]

        for x, y, bad in pairs:
            i = 0
            while i < n:
                while i < n and s[i] == bad:
                    i += 1
                if i == n:
                    break

                first = {0: i - 1}
                diff = 0

                j = i
                while j < n and s[j] != bad:
                    if s[j] == x:
                        diff += 1
                    else:
                        diff -= 1

                    if diff not in first:
                        first[diff] = j
                    else:
                        ans = max(ans, j - first[diff])

                    j += 1

                i = j

        ca = cb = cc = 0
        first = {(0, 0): -1}

        for i, ch in enumerate(s):
            if ch == 'a':
                ca += 1
            elif ch == 'b':
                cb += 1
            else:
                cc += 1

            key = (ca - cb, ca - cc)

            if key not in first:
                first[key] = i
            else:
                ans = max(ans, i - first[key])

        return ans