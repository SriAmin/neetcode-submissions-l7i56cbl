class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        l, r = 0, N - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        
        for i in range(N):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]