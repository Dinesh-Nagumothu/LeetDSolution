from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        
        odd_freqs = [count for count in freq.values() if count % 2 == 1]
        even_freqs = [count for count in freq.values() if count % 2 == 0]
        
        # If we have no odd or no even frequencies, no valid pair exists
        if not odd_freqs or not even_freqs:
            return 0
        
        # Find the max difference
        max_diff = max(a1 - a2 for a1 in odd_freqs for a2 in even_freqs)
        return max_diff
