from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        digit_count = Counter(digits)

        # Iterate all 3-digit numbers from 100 to 998 (even only)
        for num in range(100, 1000, 2):
            num_digits = [int(d) for d in str(num)]
            num_count = Counter(num_digits)

            # Check if num_digits can be formed from input digits
            if all(num_count[d] <= digit_count[d] for d in num_count):
                result.add(num)

        return sorted(result)
