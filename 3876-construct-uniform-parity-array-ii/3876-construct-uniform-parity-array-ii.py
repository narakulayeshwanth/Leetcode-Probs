class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2:
                min_odd = min(min_odd, x)
            else:
                min_even = min(min_even, x)

        # All odd
        if min_even == float('inf'):
            return True

        # All even
        if min_odd == float('inf'):
            return True

        # Make every element odd
        return min_odd < min_even