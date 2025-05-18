MOD = 10**9 + 7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from itertools import product

        # Generate all valid patterns for a single column
        def generate_patterns():
            patterns = []
            for colors in product(range(3), repeat=m):
                if all(colors[i] != colors[i+1] for i in range(m - 1)):
                    patterns.append(colors)
            return patterns

        # Precompute compatibility between patterns
        def compute_compatibility(patterns):
            compat = {}
            for p1 in patterns:
                compat[p1] = []
                for p2 in patterns:
                    if all(a != b for a, b in zip(p1, p2)):
                        compat[p1].append(p2)
            return compat

        patterns = generate_patterns()
        compat = compute_compatibility(patterns)

        # Initialize dp with count 1 for each pattern
        dp = {p: 1 for p in patterns}

        for _ in range(n - 1):
            new_dp = {p: 0 for p in patterns}
            for p in patterns:
                for q in compat[p]:
                    new_dp[q] = (new_dp[q] + dp[p]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
