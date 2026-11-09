class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #go through queres 
        preMap = {i: [] for i in range(numCourses)}
        for req, course in prerequisites:
            preMap[req].append(course)
        
        answer = []

        def isprereq(prereq, crs):
            if preMap[prereq] != [] and prereq not in visited:
                visited.add(prereq)
                for course in preMap[prereq]:
                    if course == crs:
                        return True
                    else:
                        if isprereq(course, crs):
                            return True
            return False

        for querie in queries:
            visited = set()
            prereq, crs = querie
            if isprereq(prereq, crs):
                answer.append(True)
            else:
                answer.append(False)
                
        return answer