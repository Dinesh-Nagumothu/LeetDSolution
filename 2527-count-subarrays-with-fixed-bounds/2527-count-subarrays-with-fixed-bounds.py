class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_minK = last_maxK = last_invalid = -1
        count = 0
        
        for i, num in enumerate(nums):
            # If the number is out of the bounds of [minK, maxK], reset positions
            if num < minK or num > maxK:
                last_invalid = i
            
            # Update the last position of minK and maxK
            if num == minK:
                last_minK = i
            if num == maxK:
                last_maxK = i
                
            # Count the number of valid subarrays ending at i
            if last_minK != -1 and last_maxK != -1:
                count += max(0, min(last_minK, last_maxK) - last_invalid)
        
        return count
