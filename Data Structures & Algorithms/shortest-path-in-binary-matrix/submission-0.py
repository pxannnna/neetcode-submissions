from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # If the start or end is blocked, no path exists
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        
        # Queue stores: (row, col, current_path_length)
        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}
        directions = [[1,0], [-1,0], [0, 1], [0,-1], [1,1], [-1,1], [-1,-1], [1,-1]]
        
        while queue:
            row, col, dist = queue.popleft()
            
            # If we reached the bottom-right, this is guaranteed to be the shortest path
            if row == rows - 1 and col == cols - 1:
                return dist
                
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                # Check bounds first, then if it's open, then if it's unvisited
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
                    
        return -1
