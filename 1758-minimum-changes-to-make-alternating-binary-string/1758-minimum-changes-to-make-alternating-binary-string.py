class Solution:
    def minOperations(self, s: str) -> int:
        cnt = 0

        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                cnt += 1

        return min(cnt, len(s) - cnt)