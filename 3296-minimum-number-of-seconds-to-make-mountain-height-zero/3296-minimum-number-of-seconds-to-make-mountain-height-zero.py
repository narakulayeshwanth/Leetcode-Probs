from math import isqrt

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(time):
            total = 0

            for w in workerTimes:
                d = 1 + (8 * time) // w
                x = (isqrt(d) - 1) // 2

                while w * x * (x + 1) // 2 > time:
                    x -= 1
                while w * (x + 1) * (x + 2) // 2 <= time:
                    x += 1

                total += x
                if total >= mountainHeight:
                    return True

            return False

        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left