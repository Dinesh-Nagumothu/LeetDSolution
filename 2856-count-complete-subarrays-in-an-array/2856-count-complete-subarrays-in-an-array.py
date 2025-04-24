class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        total_distinct = len(set(nums))  # total distinct elements in the whole array

        for i in range(n):
            freq = set()
            for j in range(i, n):
                freq.add(nums[j])
                if len(freq) == total_distinct:
                    total += 1
        return total
