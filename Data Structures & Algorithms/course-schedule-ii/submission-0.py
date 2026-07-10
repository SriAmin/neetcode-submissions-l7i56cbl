class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            courses[crs].append(pre)
        
        output = []
        visit, cycle = set(), set()

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            cycle.add(c)
            for pre in courses[c]:
                if not dfs(pre):
                    return False
            cycle.remove(c)
            visit.add(c)
            output.append(c)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output