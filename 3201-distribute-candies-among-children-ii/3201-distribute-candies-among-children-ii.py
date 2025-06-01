class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def count_ways(n):
            return comb(n + 2, 2) if n >= 0 else 0

        total = count_ways(n)
        
        # Subtract cases where one child exceeds the limit
        for i in range(3):
            total -= count_ways(n - (limit + 1))
        
        # Add back cases where two children exceed the limit (over-subtracted)
        for i in range(3):
            for j in range(i + 1, 3):
                total += count_ways(n - 2 * (limit + 1))
        
        # Subtract cases where all three children exceed the limit (if applicable)
        if n - 3 * (limit + 1) >= 0:
            total -= count_ways(n - 3 * (limit + 1))

        return total
