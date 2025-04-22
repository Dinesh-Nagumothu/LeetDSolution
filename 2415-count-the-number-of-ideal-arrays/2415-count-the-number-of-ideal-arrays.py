class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        # 1. Determine max exponent possible for any number up to maxValue
        import math
        max_exp = int(math.log2(maxValue)) + 1  # rough upper bound

        # We will need factorials up to (n + max_exp - 1)
        max_fact = n + max_exp

        # 2. Precompute factorials and inverse factorials
        fact = [1] * (max_fact + 1)
        for i in range(1, max_fact + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (max_fact + 1)
        inv_fact[max_fact] = pow(fact[max_fact], MOD - 2, MOD)
        for i in range(max_fact - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def nCr(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        # 3. Generate prime exponent list for numbers up to maxValue
        exponents = [[] for _ in range(maxValue + 1)]
        for p in range(2, maxValue + 1):
            if not exponents[p]:  # p is prime
                for multiple in range(p, maxValue + 1, p):
                    x, count = multiple, 0
                    while x % p == 0:
                        x //= p
                        count += 1
                    exponents[multiple].append(count)

        # 4. Count valid ideal arrays
        total = 0
        for x in range(1, maxValue + 1):
            ways = 1
            for e in exponents[x]:
                ways = ways * nCr(n + e - 1, e) % MOD
            total = (total + ways) % MOD

        return total
