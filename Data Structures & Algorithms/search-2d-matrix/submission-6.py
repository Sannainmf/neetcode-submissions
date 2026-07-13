class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        numRows = len(matrix)
        numCols = len(matrix[0])

        l = 0
        r = numRows * numCols - 1

        """
        11 != 10 it is greater. So we do r = 4

        """
        
        while l <= r:
            middle = (l + r) // 2
            rowIndex = middle // numCols
            colIndex = middle % numCols
            if matrix[rowIndex][colIndex] == target:
                return True
            elif matrix[rowIndex][colIndex] > target:
                r = middle - 1
            else:
                l = middle + 1

        return False
