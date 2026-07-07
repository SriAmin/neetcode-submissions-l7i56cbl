class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        pacific = set()
        atlantic = set()

        for i in range(m):
            pacific.add((0, i))
            atlantic.add((n-1, i))

        for i in range(n):
            pacific.add((i, 0))
            atlantic.add((i, m-1))
        
        def dfs(row, col, visited, res):
            if (row, col) in visited:
                return
            res.add((row, col))
            visited.add((row, col))
            
            neighbors = [[row + 1, col], [row - 1, col], [row, col+1], [row, col-1]]
            for n_row, n_col in neighbors:
                if min(n_row, n_col) < 0 or n_row >= n or n_col >= m or heights[n_row][n_col] < heights[row][col]:
                    continue
                dfs(n_row, n_col, visited, res)
        
        pacific_res = set()
        atlantic_res = set()
        for x, y in pacific:
            dfs(x, y, set(), pacific_res)
        for x, y in atlantic:
            dfs(x, y, set(), atlantic_res)

        print(pacific_res)
        print(atlantic_res)
            
        return list(pacific_res.intersection(atlantic_res))
        