class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        pacific, atlantic = set(), set()
        
        def dfs(row, col, visited, prevHeight):
            if (row, col) in visited or min(row, col) < 0 or row >= n or col >= m or heights[row][col] < prevHeight:
                return
            visited.add((row, col))
            
            neighbors = [[row + 1, col], [row - 1, col], [row, col+1], [row, col-1]]
            for n_row, n_col in neighbors:
                dfs(n_row, n_col, visited, heights[row][col])

        for i in range(m):
            dfs(0, i, pacific, heights[0][i])
            dfs(n - 1, i, atlantic, heights[n-1][i])

        for i in range(n):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, m-1, atlantic, heights[i][m-1])
        
        res = []
        for r in range(n):
            for c in range(m):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
            
        return res
        