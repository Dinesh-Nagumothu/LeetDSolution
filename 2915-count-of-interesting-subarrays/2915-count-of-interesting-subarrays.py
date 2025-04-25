class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1  # Initial prefix is 0 (no matching element yet)

        for num in nums:
            if num % modulo == k:
                prefix += 1

            # We want to find previous prefix such that:
            # prefix[j] % modulo == (prefix - k + modulo) % modulo
            target = (prefix - k + modulo) % modulo
            count += freq[target]
            freq[prefix % modulo] += 1

        return count
