class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        c = Counter(answers)
        for k, v in c.items():
            q, r = divmod(v, k+1)
            ans += q*(k+1) + ((k+1) if r > 0 else 0)
        return ans