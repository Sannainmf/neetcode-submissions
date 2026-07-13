class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        fullList = []

        for l in matrix:
            fullList += l

        left = 0
        right = len(fullList) - 1

        while left <= right:
            mid = (left + right) // 2
            if fullList[mid] == target:
                return True
            elif fullList[mid] > target:
                right = mid - 1
            elif fullList[mid] < target:
                left = mid + 1

        return False
        