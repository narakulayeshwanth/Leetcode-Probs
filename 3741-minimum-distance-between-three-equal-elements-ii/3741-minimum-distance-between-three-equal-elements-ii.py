from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = [[] for _ in range(len(nums) + 1)]

        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = float("inf")

        for indices in pos:
            for i in range(len(indices) - 2):
                ans = min(ans, 2 * (indices[i + 2] - indices[i]))

        return -1 if ans == float("inf") else ans