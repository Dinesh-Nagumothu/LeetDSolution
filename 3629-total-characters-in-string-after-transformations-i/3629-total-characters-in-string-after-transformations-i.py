class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7

        # dp[i] means the resulting length of character 'a' + i after t transformations
        dp = [1] * 26  # Initial lengths: every character maps to length 1

        for _ in range(t):
            new_dp = [0] * 26
            for i in range(26):
                if i == 25:  # 'z'
                    new_dp[i] = (dp[0] + dp[1]) % MOD  # 'z' becomes 'ab'
                else:
                    new_dp[i] = dp[i + 1]  # other chars just become next char
            dp = new_dp

        total = 0
        for ch in s:
            total = (total + dp[ord(ch) - ord('a')]) % MOD

        return total
