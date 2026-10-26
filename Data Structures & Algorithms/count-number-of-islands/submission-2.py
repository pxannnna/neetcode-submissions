from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()


        def bfs(row, col):
            if not grid:
                return 0
            queue = deque([(row,col)])
            visited.add((row,col))
            directions = [[1,0], [-1,0], [0,1], [0, -1]]
            while queue:
                for _ in range(len(queue)):
                    r,c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = dr+ r, dc + c
                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                            visited.add((nr,nc))
                            queue.append((nr,nc))
                            
            
        for r in range(rows):
            for l in range(cols):
                if grid[r][l] == "1" and (r,l) not in visited:
                    bfs(r,l)
                    islands += 1
        return islands


