class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0

            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0

            return (1 + dfs(i + 1, j) + 
                        dfs(i, j + 1) + 
                        dfs(i - 1, j) + 
                        dfs(i, j - 1))


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea