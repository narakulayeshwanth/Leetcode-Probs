class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        # Try to keep target's prefix equal.
        for i in range(n - 1, -1, -1):
            # Reconstruct remaining characters for target[:i]
            freq = cnt[:]
            possible = True

            for j in range(i):
                x = ord(target[j]) - ord('a')

                if freq[x] == 0:
                    possible = False
                    break

                freq[x] -= 1

            if not possible:
                continue

            # Find smallest character > target[i]
            cur = ord(target[i]) - ord('a')

            for c in range(cur + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1

                    # Put remaining characters in sorted order
                    result = target[:i] + chr(c + ord('a'))

                    for x in range(26):
                        result += chr(x + ord('a')) * freq[x]

                    return result

        return ""