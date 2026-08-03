from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)

        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = float('inf')

        for indices in pos.values():
            for i in range(len(indices) - 2):
                distance = 2 * (indices[i + 2] - indices[i])
                ans = min(ans, distance)

        return -1 if ans == float('inf') else ans