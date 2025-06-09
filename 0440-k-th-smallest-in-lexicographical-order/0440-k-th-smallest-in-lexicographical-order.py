class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix, n):
            """Count steps between prefix and prefix + 1 within range [1, n]"""
            steps = 0
            first = prefix
            last = prefix + 1
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
            return steps

        curr = 1
        k -= 1  # we already start from 1

        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1  # go to next prefix
            else:
                curr *= 10  # go deeper
                k -= 1

        return curr
