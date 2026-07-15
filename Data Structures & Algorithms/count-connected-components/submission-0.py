class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        res = 0
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh, node)

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i, 0)
        return res