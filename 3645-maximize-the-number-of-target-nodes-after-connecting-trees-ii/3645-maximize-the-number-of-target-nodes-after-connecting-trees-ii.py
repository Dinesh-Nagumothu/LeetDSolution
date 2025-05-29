from collections import deque

class Solution:
    def __init__(self):
        self.evenA = 0
        self.oddA = 0
        self.evenB = 0
        self.oddB = 0

    def buildList(self, edges):
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def bfsColor(self, adj, color, isA):
        queue = deque([0])
        color[0] = 0

        while queue:
            u = queue.popleft()
            if color[u] == 0:
                if isA:
                    self.evenA += 1
                else:
                    self.evenB += 1
            else:
                if isA:
                    self.oddA += 1
                else:
                    self.oddB += 1

            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    queue.append(v)

    def maxTargetNodes(self, edges1, edges2):
        adjA = self.buildList(edges1)
        adjB = self.buildList(edges2)
        n, m = len(adjA), len(adjB)
        colorA = [-1] * n
        colorB = [-1] * m

        self.evenA = self.oddA = self.evenB = self.oddB = 0
        self.bfsColor(adjA, colorA, True)
        self.bfsColor(adjB, colorB, False)

        maxiB = max(self.evenB, self.oddB)
        return [(self.evenA if colorA[i] == 0 else self.oddA) + maxiB for i in range(n)]