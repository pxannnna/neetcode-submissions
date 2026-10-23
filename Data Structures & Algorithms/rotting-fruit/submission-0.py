from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        
        # 1. Add all starting rotten fruits to the queue and count fresh fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # 2. Process BFS level by level (minute by minute)
        while q and fresh > 0:
            for _ in range(len(q)):  # Process all fruits rotting in the current minute
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2  # Turn fresh fruit rotten
                        fresh -= 1
                        q.append((row, col))
            time += 1  # One minute has elapsed
            
        return time if fresh == 0 else -1
