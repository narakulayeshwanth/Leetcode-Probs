from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Put min_idx first and max_idx second
        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx

        # 1. Remove both from the front
        front = max_idx + 1

        # 2. Remove both from the back
        back = n - min_idx

        # 3. Remove min from front and max from back
        mixed = (min_idx + 1) + (n - max_idx)

        return min(front, back, mixed)