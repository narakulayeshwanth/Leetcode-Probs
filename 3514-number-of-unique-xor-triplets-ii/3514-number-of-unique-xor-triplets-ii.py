class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        dp = [set() for _ in range(4)]
        dp[0].add(0)

        for v in nums:
            for k in range(2, -1, -1):
                if dp[k]:
                    dp[k + 1] |= {x ^ v for x in dp[k]}

        return len(dp[1] | dp[3])