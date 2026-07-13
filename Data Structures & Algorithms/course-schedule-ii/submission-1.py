class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for course, preq in prerequisites:
            indegree[course] += 1
            preqs[preq].append(course)
        print(preqs)
        print(indegree)
        res = []

        def dfs(c):
            res.append(c)
            indegree[c] -= 1
            for preq in preqs[c]:
                indegree[preq] -= 1
                if indegree[preq] == 0:
                    dfs(preq)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        print(res)
        return res if len(res) == numCourses else []