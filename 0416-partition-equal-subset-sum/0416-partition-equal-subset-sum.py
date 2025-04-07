class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # If total sum is odd, we cannot split it into two equal subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        # Use a set to store achievable subset sums
        possible_sums = set()
        possible_sums.add(0)

        for num in nums:
            current_sums = set()
            for s in possible_sums:
                if s + num == target:
                    return True
                current_sums.add(s + num)
                current_sums.add(s)
            possible_sums = current_sums

        return target in possible_sums