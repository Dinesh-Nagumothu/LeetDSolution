class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        total = 0
        
        for answer, count in counter.items():
            group_size = answer + 1
            groups = ceil(count / group_size)
            total += groups * group_size
        
        return total
