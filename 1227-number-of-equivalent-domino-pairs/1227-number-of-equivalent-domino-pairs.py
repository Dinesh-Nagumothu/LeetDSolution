
from collections import Counter

class Solution:
    
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        dominoes = [ (e[0] << 4) + e[1] if e[0] < e[1] else (e[1] << 4) + e[0] for e in dominoes]
        counter = Counter(dominoes)
        result = 0
        for key, value in counter.items():
            if value >= 2:
                result += value * (value - 1) >> 1
        return result