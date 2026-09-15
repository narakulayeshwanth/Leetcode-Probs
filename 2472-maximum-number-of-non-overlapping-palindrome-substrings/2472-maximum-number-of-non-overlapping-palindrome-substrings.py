class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # latest[r] = largest starting index of a palindrome
        # of length >= k that ends at r
        latest = [-1] * n

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    latest[r] = max(latest[r], l)
                l -= 1
                r += 1

        # Odd length palindromes
        for i in range(n):
            expand(i, i)

        # Even length palindromes
        for i in range(n - 1):
            expand(i, i + 1)

        # dp[i] = maximum number of palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't select a palindrome ending at i-1
            dp[i] = dp[i - 1]

            start = latest[i - 1]

            if start != -1:
                dp[i] = max(dp[i], dp[start] + 1)

        return dp[n]