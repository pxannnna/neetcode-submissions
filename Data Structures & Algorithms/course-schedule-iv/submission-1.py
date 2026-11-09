from collections import deque
from typing import List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize graph, in-degrees, and prerequisite sets
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        prereqs = [set() for _ in range(numCourses)]
        
        # Build the graph and count in-degrees
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1 
        # Add all courses with no prerequisites to the queue
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                prereqs[v].add(u)
                prereqs[v].update(prereqs[u])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)          
        answer = []
        for u, v in queries:
            if u in prereqs[v]:
                answer.append(True)
            else:
                answer.append(False)      
        return answer
