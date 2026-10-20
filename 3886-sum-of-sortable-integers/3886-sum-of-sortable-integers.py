from typing import List
from collections import Counter

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        def is_rotation(a, b):
            k = len(a)
            if Counter(a) != Counter(b):
                return False

            # KMP prefix function for b
            pi = [0] * k
            j = 0
            for i in range(1, k):
                while j and b[i] != b[j]:
                    j = pi[j - 1]
                if b[i] == b[j]:
                    j += 1
                pi[i] = j

            # Search b in a + a, without constructing it
            j = 0
            for i in range(2 * k - 1):
                x = a[i % k]
                while j and x != b[j]:
                    j = pi[j - 1]
                if x == b[j]:
                    j += 1
                if j == k:
                    return True
            return False

        for k in range(1, n + 1):
            if n % k:
                continue

            valid = True
            for start in range(0, n, k):
                if not is_rotation(nums[start:start + k],
                                   target[start:start + k]):
                    valid = False
                    break

            if valid:
                ans += k

        return ans