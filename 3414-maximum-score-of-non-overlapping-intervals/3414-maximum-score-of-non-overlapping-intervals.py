from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # [left, right, weight, original_index]
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by right endpoint
        arr.sort(key=lambda x: x[1])

        rights = [x[1] for x in arr]

        # prev[i] = number of intervals ending before arr[i] starts
        prev = [0] * n
        for i in range(n):
            l = arr[i][0]
            prev[i] = bisect_left(rights, l)

        # dp[k][i] = best result using at most k intervals
        # among the first i intervals
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):
                # Don't take current interval
                best_score, best_indices = dp[k][i - 1]

                # Take current interval
                idx = i - 1
                l, r, w, original_index = arr[idx]

                p = prev[idx]

                old_score, old_indices = dp[k - 1][p]
                take_score = old_score + w
                take_indices = tuple(sorted(old_indices + (original_index,)))

                # Choose maximum score.
                # If scores are equal, choose lexicographically smaller indices.
                if (take_score > best_score or
                    (take_score == best_score and take_indices < best_indices)):
                    best_score = take_score
                    best_indices = take_indices

                dp[k][i] = (best_score, best_indices)

        return list(dp[4][n][1])