class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        # Check whether a palindrome is possible
        odd = -1

        for i in range(26):
            if cnt[i] % 2 == 1:
                if odd != -1:
                    return ""
                odd = i

        half_len = n // 2

        # Counts for the first half
        half_cnt = [x // 2 for x in cnt]

        def build(left):
            ans = ''.join(chr(x + ord('a')) for x in left)

            if n % 2:
                ans += chr(odd + ord('a'))

            ans += ''.join(chr(x + ord('a')) for x in reversed(left))

            return ans

        # Try every possible position where the palindrome
        # becomes greater than target.
        for i in range(half_len, -1, -1):
            freq = half_cnt[:]
            left = []
            possible = True

            # Match target's prefix exactly
            for j in range(i):
                x = ord(target[j]) - ord('a')

                if freq[x] == 0:
                    possible = False
                    break

                freq[x] -= 1
                left.append(x)

            if not possible:
                continue

            # If i == half_len, we matched the entire left half.
            # Check whether the resulting palindrome is already greater.
            if i == half_len:
                candidate = build(left)

                if candidate > target:
                    return candidate

                continue

            # Make the current character minimally larger
            target_char = ord(target[i]) - ord('a')

            for c in range(target_char + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1

                    new_left = left + [c]

                    # Fill the rest with the smallest characters
                    for x in range(26):
                        new_left.extend([x] * freq[x])

                    return build(new_left)

        return ""