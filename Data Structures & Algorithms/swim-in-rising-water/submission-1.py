class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        visited.add((0,0))
        largest_time = 0
        min_heap = [(grid[0][0], 0, 0)]
        directions = [[1,0], [-1,0], [0,1], [0,-1]]


        #we consider each neighbour -> find the smalled height using heap -> 
        # update maximum number for time
        # add to visited -> explore neighbours

        while min_heap: 
            height, r, c = heapq.heappop(min_heap)
            largest_time = max(height, largest_time)

            if (r,c) == (rows-1, cols-1):
                return largest_time

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
            
        return largest_time
