class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        def addCell(nr, nc):
            if (min(nr, nc) < 0 or nr == n or nc == m or (nr, nc) in visited or grid[nr][nc] == -1):
                return
            visited.add((nr, nc))
            q.append([nr, nc])

        dis = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dis

                neighbors = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]
                for nr, nc in neighbors:
                    addCell(nr, nc)
            dis += 1