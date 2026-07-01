class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        freshfruit = 0
        time = 0

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    freshfruit += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        time = 0
        while freshfruit > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
                neighbors = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]
                for nr, nc in neighbors:
                    if (nr in range(n) and nc in range(m) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        freshfruit -= 1
            time += 1
        return time if freshfruit == 0 else -1
