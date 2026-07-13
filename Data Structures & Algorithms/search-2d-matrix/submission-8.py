class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:



        lenRows = len(matrix)
        lenCols = len(matrix[0])
        l = 0 
        r = lenRows * lenCols - 1

        while l <= r:
            middle = (l + r) // 2
            rowIndex = middle // lenCols
            colIndex = middle % lenCols
            if matrix[rowIndex][colIndex] == target:
                return True
            elif matrix[rowIndex][colIndex] > target:
                r = middle - 1
            else:
                l = middle + 1

        return False



        