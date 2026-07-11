class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        seen = set()
        mask = (1 << k) - 1
        val = 0

        for i in range(len(s)):
            val = ((val << 1) & mask) | (ord(s[i]) - ord('0'))

            if i >= k - 1:
                seen.add(val)

        return len(seen) == (1 << k)