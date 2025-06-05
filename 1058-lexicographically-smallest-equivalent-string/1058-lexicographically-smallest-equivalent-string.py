class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]  # For 'a' to 'z'

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return
            # Always keep the smaller character as the parent
            if rootX < rootY:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY

        # Process equivalences
        for ch1, ch2 in zip(s1, s2):
            union(ord(ch1) - ord('a'), ord(ch2) - ord('a'))

        # Transform baseStr
        result = []
        for ch in baseStr:
            smallest = chr(find(ord(ch) - ord('a')) + ord('a'))
            result.append(smallest)

        return ''.join(result)
