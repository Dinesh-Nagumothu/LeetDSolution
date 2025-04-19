class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n):
            # We want to find the number of j > i such that:
            # lower - nums[i] <= nums[j] <= upper - nums[i]
            left = bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect_right(nums, upper - nums[i], i + 1, n)
            count += (right - left)
        
        return count
