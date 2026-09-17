from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        # best[i] = minimum length of a target-sum subarray
        # completely inside arr[0:i]
        best = [INF] * (n + 1)

        left = 0
        curr = 0
        ans = INF

        for right in range(n):
            curr += arr[right]

            while curr > target:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1

                # A previous subarray must end before `left`
                if best[left] != INF:
                    ans = min(ans, length + best[left])

                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if ans == INF else ans