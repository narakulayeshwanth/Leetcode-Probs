class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:
                # Remove unnecessary leading zeros
                start = left
                while start <= right and s[start] == '0':
                    start += 1

                current = s[start:right + 1]

                if best == "" or len(current) < len(best):
                    best = current
                elif len(current) == len(best) and current < best:
                    best = current

        return best