class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        difference_array = [0] * (n + 1)

        # Process query
        for start, end in queries:
            # Process start and end of range
            difference_array[start] += 1
            difference_array[end + 1] -= 1

        total_sum = 0
        for i in range(n):
            total_sum += difference_array[i]
            if total_sum < nums[i]:
                return False
        
        return True
        