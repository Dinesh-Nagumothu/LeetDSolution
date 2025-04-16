class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Initialize the frequency map, number of pairs, and result
        freq = defaultdict(int)
        pairs = 0
        result = 0
        left = 0
        
        # Iterate over the array with a sliding window approach
        for right in range(len(nums)):
            # Add the current number to the frequency map
            num = nums[right]
            # If num was seen before, we can form pairs with the previous occurrences of num
            pairs += freq[num]
            # Increment the frequency of the current number
            freq[num] += 1
            
            # While the number of pairs is >= k, shrink the window from the left
            while pairs >= k:
                # If we found a valid subarray, add the number of subarrays ending at `right`
                result += len(nums) - right
                # Reduce the pair count by removing the leftmost element
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1
        
        return result
