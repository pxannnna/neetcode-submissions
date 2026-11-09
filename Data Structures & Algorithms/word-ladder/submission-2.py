from collections import deque
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbors = defaultdict(list)
        for word in wordList:
            for c in range(len(word)):
                newword = word[:c] + "*" + word[c+1:]
                neighbors[newword].append(word)

        #neighbors["*at"] = ["cat", "bat"]

        #BFS for shortest path

        queue = deque([beginWord])
        visited = set([beginWord])
        count = 1

        while queue:
            for _ in range(len(queue)):
                currword = queue.popleft()
                if currword == endWord:
                        return count
                
                for c in range(len(currword)):
                    newword = currword[:c] + "*" + currword[c+1:]
                    for neighbor in neighbors[newword]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            count += 1
        return 0
                            
                            




                

