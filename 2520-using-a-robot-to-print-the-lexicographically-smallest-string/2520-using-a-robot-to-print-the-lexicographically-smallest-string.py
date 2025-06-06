class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        result = []
        t = []
        
        # Step 1: Create min_suffix array
        min_suffix = [None] * n
        min_suffix[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])
        
        # Step 2: Greedy simulation
        for i in range(n):
            t.append(s[i])
            # While we can pop from t to write to result
            while t and (i == n - 1 or t[-1] <= min_suffix[i + 1]):
                result.append(t.pop())
        
        return ''.join(result)
