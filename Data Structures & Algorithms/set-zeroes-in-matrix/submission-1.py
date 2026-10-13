class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        M = len(matrix[0])
        rowZero = False

        for r in range(N):
            for c in range(M):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        for r in range(1, N):
            for c in range(1, M):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(N):
                matrix[r][0] = 0
        if rowZero:
            for c in range(M):
                matrix[0][c] = 0
                    

        