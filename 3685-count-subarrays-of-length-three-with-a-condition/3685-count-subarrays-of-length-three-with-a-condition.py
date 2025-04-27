class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(1, n - 1):
            if nums[i] % 2 == 0 and (nums[i - 1] + nums[i + 1]) == (nums[i] // 2):
                count += 1
        
        return count
