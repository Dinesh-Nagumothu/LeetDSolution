class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i] will be the size of the largest subset ending with nums[i]
        prev = [-1] * n  # To reconstruct the path
        max_idx = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i

        # Reconstruct the subset
        res = []
        k = max_idx
        while k >= 0:
            res.append(nums[k])
            k = prev[k]

        return res[::-1]  # Reverse to return in increasing order
