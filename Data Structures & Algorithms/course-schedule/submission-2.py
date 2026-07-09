class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        for i in range(len(prerequisites)):
            c, p = prerequisites[i][0], prerequisites[i][1]
            if c not in courses:
                courses[c] = []
            courses[c].append(p)
        
        path = set()
        
        def dfs(course):
            if course in path:
                return False
                
            if course not in courses:
                return True

            preqs = courses[course]
            path.add(course)

            for p in preqs:
                if not dfs(p):
                    return False
            path.remove(course)
            courses[course] = []
            return True
        
        for c in prerequisites:
            if not dfs(c[0]):
                return False
        
        return True