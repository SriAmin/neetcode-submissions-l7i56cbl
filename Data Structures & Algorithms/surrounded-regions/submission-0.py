class Solution:
    def solve(self, board: List[List[str]]) -> None:
        regions = []
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        border = [
            (r, c) for r in range(ROWS) for c in range(COLS)
            if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1
        ]

        def dfs(row, col):
            board[row][col] = "#"
            neighbors = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]

            for n_row, n_col in neighbors:
                if min(n_row, n_col) == 0 or n_row >= ROWS or n_col >= COLS:
                    continue
                if board[n_row][n_col] == "O":
                    dfs(n_row, n_col)

        for cell_x, cell_y in border:
            if board[cell_x][cell_y] == "O":
                dfs(cell_x, cell_y)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O": board[r][c] = "X"
                if board[r][c] == "#": board[r][c] = "O"
        
        