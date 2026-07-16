from math import gcd
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefix = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            prefix.append(gcd(x, mx))

        prefix.sort()

        i, j = 0, len(prefix) - 1
        ans = 0

        while i < j:
            ans += gcd(prefix[i], prefix[j])
            i += 1
            j -= 1

        return ans