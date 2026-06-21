class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordLen = len(word)
        n = len(board)
        m = len(board[0])

        if wordLen > n * m:
            return False
        
        def findMatch(row, col, wIdx):
            if wIdx == wordLen:
                return True
            
            if row < 0 or col < 0 or row >= n or col >= m:
                return False

            if board[row][col] == word[wIdx]:
                tmpChar = board[row][col]
                board[row][col] = "#"

                res = findMatch(row + 1, col, wIdx + 1) or findMatch(row, col + 1, wIdx + 1) or findMatch(row - 1, col, wIdx + 1) or findMatch(row, col - 1, wIdx + 1)
                board[row][col] = tmpChar
                return res
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if findMatch(i, j, 0):
                        return True
        return False