class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                else:
                    if parent != neighbor:
                        return True
            return False

        if dfs(0, -1):
            return False
        return len(visited) == n
            
