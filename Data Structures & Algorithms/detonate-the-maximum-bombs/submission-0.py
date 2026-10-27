from collections import defaultdict
from typing import List


class Solution:

  def maximumDetonation(self, bombs: List[List[int]]) -> int:
    detonationmap = defaultdict(list)
    n = len(bombs)

    # 1. Build adjacency list using integer indices 0 to n-1
    for i in range(n):
      x1, y1, r1 = bombs[i]
      for j in range(n):
        if i == j:
          continue
        x2, y2, _ = bombs[j]

        distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
        if r1**2 >= distance:
          detonationmap[i].append(j)

    # 2. DFS helper taking node index
    def dfs(node, visited):
      visited.add(node)
      for neighbor in detonationmap[node]:
        if neighbor not in visited:
          dfs(neighbor, visited)

    maxcount = 0

    # 3. Outer loop: Try detonating every bomb first
    for i in range(n):
      visited = set()  # Fresh set for each trial run
      dfs(i, visited)
      maxcount = max(maxcount, len(visited))  # Number of detonated bombs

    return maxcount
