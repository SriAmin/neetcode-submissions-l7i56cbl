class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i:0 for i in range(numCourses)}
        preqs = {i:[] for i in range(numCourses)}
        res = []
        for course, preq in prerequisites:
            indegree[course] += 1
            preqs[preq].append(course)

        def dfs(c):
            res.append(c)
            indegree[c] -= 1

            for preq in preqs[c]:
                indegree[preq] -= 1
                if indegree[preq] == 0:
                    dfs(preq)

        for course in range(numCourses):
            if indegree[course] == 0:
                dfs(course)
        print(res)
        return res if len(res) == numCourses else []