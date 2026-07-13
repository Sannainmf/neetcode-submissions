class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        fullList = []

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                item = matrix[row][col]
                fullList.append(item)

        l = 0
        r = len(fullList) - 1

        while l <= r:
            middle = (l + r) // 2
            if fullList[middle] == target:
                return True
            elif fullList[middle] > target:
                r = middle - 1
            else:
                l = middle + 1

        return False