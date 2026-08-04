from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        lo = min(nums)
        hi = max(nums)

        ans = []
        for x in range(lo, hi + 1):
            if x not in s:
                ans.append(x)

        return ans