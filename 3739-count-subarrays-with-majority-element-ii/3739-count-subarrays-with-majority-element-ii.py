class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        offset = n + 2
        size = 2 * n + 5
        bit = [0] * size
        def update(i):
            while i < size:
                bit[i] += 1
                i += i & -i
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        pref = 0
        ans = 0
        update(offset)
        for x in nums:
            if x == target:
                pref += 1
            else:
                pref -= 1
            idx = pref + offset
            ans += query(idx - 1)
            update(idx)
        return ans