from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_position(s: int) -> (int, int):
            # Convert square number to board coordinates
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if (quot % 2 == 0) else (n - 1 - rem)
            return row, col
        
        visited = set()
        queue = deque([(1, 0)])  # (square, number of moves)

        while queue:
            s, moves = queue.popleft()
            for next_s in range(s + 1, min(s + 6, n * n) + 1):
                r, c = get_position(next_s)
                dest = board[r][c] if board[r][c] != -1 else next_s
                if dest == n * n:
                    return moves + 1
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))
                    
        return -1
