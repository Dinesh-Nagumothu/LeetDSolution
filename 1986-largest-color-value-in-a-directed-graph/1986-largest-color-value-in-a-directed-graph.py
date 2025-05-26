class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        
        # Build graph and indegree count
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # DP array: dp[i][c] -> max number of color c (0..25) along path to node i
        dp = [[0] * 26 for _ in range(n)]
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1
        
        visited = 0
        max_color_value = 0
        
        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                for c in range(26):
                    # Update neighbor's color count
                    count = dp[node][c] + (1 if c == ord(colors[neighbor]) - ord('a') else 0)
                    dp[neighbor][c] = max(dp[neighbor][c], count)
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            max_color_value = max(max_color_value, max(dp[node]))
        
        return max_color_value if visited == n else -1
