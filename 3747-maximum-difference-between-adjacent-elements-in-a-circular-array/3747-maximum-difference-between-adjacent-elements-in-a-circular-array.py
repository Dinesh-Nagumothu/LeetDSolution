class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        n = len(nums)
        for i in range(n):
            next_idx = (i + 1) % n  # ensures circular adjacency
            diff = abs(nums[i] - nums[next_idx])
            max_diff = max(max_diff, diff)
        return max_diff
