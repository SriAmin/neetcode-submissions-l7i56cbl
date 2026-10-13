class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        M = len(matrix[0])
        rows, cols = [False] * N, [False] * M

        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        for r in range(N):
            for c in range(M):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
                    

        