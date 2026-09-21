class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Factor t into 2, 3, 5, 7
        need = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i, p in enumerate(primes):
            while t % p == 0:
                need[i] += 1
                t //= p

        # Digits 1..9 cannot provide any other prime
        if t != 1:
            return "-1"

        # Factor contribution of digits
        fac = [[0] * 4 for _ in range(10)]

        for d in range(1, 10):
            x = d
            for i, p in enumerate(primes):
                while x % p == 0:
                    fac[d][i] += 1
                    x //= p

        # dp[a][b] = minimum digits needed for 2^a * 3^b
        A, B = need[0], need[1]
        INF = 10**9

        dp = [[INF] * (B + 1) for _ in range(A + 1)]
        dp[0][0] = 0

        useful = [2, 3, 4, 6, 8, 9]

        for a in range(A + 1):
            for b in range(B + 1):
                for d in useful:
                    x = fac[d][0]
                    y = fac[d][1]

                    if a >= x and b >= y:
                        dp[a][b] = min(
                            dp[a][b],
                            dp[a - x][b - y] + 1
                        )

        def min_digits(req):
            return (
                req[2] +
                req[3] +
                dp[req[0]][req[1]]
            )

        # Construct lexicographically smallest number
        # of exactly `length` digits satisfying req.
        def build(req, length):
            ans = []

            for remaining in range(length, 0, -1):
                for d in range(1, 10):
                    f = fac[d]

                    nxt = [
                        max(0, req[0] - f[0]),
                        max(0, req[1] - f[1]),
                        max(0, req[2] - f[2]),
                        max(0, req[3] - f[3])
                    ]

                    if min_digits(nxt) <= remaining - 1:
                        ans.append(str(d))
                        req = nxt
                        break

            return ''.join(ans)

        n = len(num)

        # Count factors of num
        total = [0, 0, 0, 0]
        has_zero = False

        for ch in num:
            d = ord(ch) - 48

            if d == 0:
                has_zero = True
            else:
                for j in range(4):
                    total[j] += fac[d][j]

        # num itself
        if not has_zero and all(total[i] >= need[i] for i in range(4)):
            return num

        # Try to create the smallest answer with the same length.
        prefix = total[:]

        for pos in range(n - 1, -1, -1):
            old = ord(num[pos]) - 48

            # Remove current digit from prefix.
            if old != 0:
                for j in range(4):
                    prefix[j] -= fac[old][j]

            # Prefix must be zero-free.
            if '0' in num[:pos]:
                continue

            for d in range(old + 1, 10):
                req = [
                    max(0, need[0] - prefix[0] - fac[d][0]),
                    max(0, need[1] - prefix[1] - fac[d][1]),
                    max(0, need[2] - prefix[2] - fac[d][2]),
                    max(0, need[3] - prefix[3] - fac[d][3])
                ]

                remaining = n - pos - 1

                if min_digits(req) <= remaining:
                    return (
                        num[:pos] +
                        str(d) +
                        build(req, remaining)
                    )

        # No same-length answer.
        # We may need considerably more than n+1 digits.
        min_len = min_digits(need)

        length = max(n + 1, min_len)

        return build(need, length)