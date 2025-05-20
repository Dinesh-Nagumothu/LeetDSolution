class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)  # Difference array for range update

        # Count how many times each index is covered by queries
        for l, r in queries:
            diff[l] += 1
            if r + 1 < len(diff):
                diff[r + 1] -= 1

        # Prefix sum to get frequency per index
        count = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            count[i] = curr

        # Check if we can decrement nums[i] times
        for i in range(n):
            if nums[i] > count[i]:
                return False

        return True
