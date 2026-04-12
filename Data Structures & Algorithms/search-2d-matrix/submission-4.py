class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            tmpRow = matrix[mid]
            if tmpRow[0] > target:
                r = mid - 1
            elif tmpRow[len(tmpRow) - 1] < target:
                l = mid + 1
            else:
                l = 0
                r = len(tmpRow) - 1
                while l <= r:
                    mid = l + ((r - l) // 2)
                    if tmpRow[mid] < target:
                        l = mid + 1
                    elif tmpRow[mid] > target:
                        r = mid - 1
                    else:
                        return True
                return False
        return False
