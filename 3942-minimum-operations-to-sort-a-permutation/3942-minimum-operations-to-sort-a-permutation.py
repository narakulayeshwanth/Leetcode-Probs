from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if all(x == i for i, x in enumerate(nums)):
            return 0

        # Case 1: nums is a left rotation of [0, 1, ..., n-1]
        k = nums[0]
        if all(nums[i] == (i + k) % n for i in range(n)):
            return min(n - k, k + 2)

        # Case 2: nums is a left rotation of [n-1, ..., 1, 0]
        k = n - 1 - nums[0]
        if all(nums[i] == n - 1 - ((i + k) % n)
               for i in range(n)):
            return min(k, n - k) + 1

        return -1