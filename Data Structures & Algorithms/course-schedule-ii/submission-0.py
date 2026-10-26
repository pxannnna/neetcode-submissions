class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Build adjacency list: course -> list of prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        res = []
        visit = set()  # Fully processed courses added to res
        cycle = set()  # Active path in current DFS (for cycle detection)

        def dfs(crs):
            if crs in cycle:
                return False  # Cycle detected!
            if crs in visit:
                return True   # Already processed and added to res

            cycle.add(crs)

            # Process all prerequisites first
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)   # Add course ONLY AFTER all prerequisites are added
            return True

        # Run DFS for every course
        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
