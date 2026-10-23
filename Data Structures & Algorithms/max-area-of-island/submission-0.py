from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            area = 0
            
            while q:
                row, col = q.popleft()
                area += 1
                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    # Check grid boundaries, land cell, and visited status
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        grid[nr][nc] == 1 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        
            return area

        for r in range(rows):
            for c in range(cols):
                # Only start BFS on unvisited land cells
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
                    
        return max_area
