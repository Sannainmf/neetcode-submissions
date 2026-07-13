class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])
        left = 0
        right = rows * columns - 1

        while left <= right:
            middle = (left + right) // 2
            r = middle // columns
            c = middle % columns
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = middle - 1
            else:
                left = middle + 1

        return False

        