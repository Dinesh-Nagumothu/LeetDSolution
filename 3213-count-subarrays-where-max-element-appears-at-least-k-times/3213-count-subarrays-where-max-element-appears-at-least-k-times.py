class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        n = len(nums)
        left = 0
        max_count = 0
        result = 0

        for right in range(n):
            if nums[right] == max_val:
                max_count += 1

            while max_count >= k:
                result += n - right
                if nums[left] == max_val:
                    max_count -= 1
                left += 1

        return result
