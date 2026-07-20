class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visted = [False] * (n + 1)
        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if visted[node]:
                cycleStart = node
                return True
            
            visted[node] = True
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                
                if dfs(neigh, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []