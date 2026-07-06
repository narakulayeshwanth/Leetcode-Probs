class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            even = {}
            odd = {}
            distinct_even = 0
            distinct_odd = 0
            for j in range(i, n):
                x = nums[j]
                if x % 2 == 0:
                    if x not in even:
                        even[x] = 1
                        distinct_even += 1
                    else:
                        even[x] += 1
                else:
                    if x not in odd:
                        odd[x] = 1
                        distinct_odd += 1
                    else:
                        odd[x] += 1
                if distinct_even == distinct_odd:
                    ans = max(ans, j - i + 1)
        return ans