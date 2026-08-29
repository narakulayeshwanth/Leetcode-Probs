from typing import List

class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:

        pairs = sorted((value, i) for i, value in enumerate(nums))

        ans = nums[:]
        n = len(nums)

        start = 0

        for end in range(1, n + 1):
            # End of the current connected group
            if end == n or pairs[end][0] - pairs[end - 1][0] > limit:

                # Values in this group are already sorted
                values = [pairs[i][0] for i in range(start, end)]

                # Their original positions
                indices = sorted(pairs[i][1] for i in range(start, end))

                # Assign smallest values to smallest indices
                for idx, value in zip(indices, values):
                    ans[idx] = value

                start = end

        return ans