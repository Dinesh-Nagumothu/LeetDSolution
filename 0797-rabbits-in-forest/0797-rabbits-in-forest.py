class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_map = {}
        for a in answers:
            if a in count_map:
                count_map[a] += 1
            else:
                count_map[a] = 1
        
        total = 0
        for a in count_map:
            group_size = a + 1
            num_rabbits = ((count_map[a] + group_size - 1) // group_size) * group_size
            total += num_rabbits
        
        return total
