class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        digits = []
        for _ in range(num):
            d = min(9, sum)
            digits.append(str(d))
            sum -= d

        return ''.join(digits)