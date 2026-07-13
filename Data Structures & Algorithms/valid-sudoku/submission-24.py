class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            arr = []
            for j in range(len(board)):
                element = board[i][j]

                if element == ".":
                    continue
                else:
                    if element not in arr:
                        arr.append(element)
                    else:
                        return False

        for i in range(len(board)):
            arr = []
            for j in range(len(board)):
                element = board[j][i]

                if element == ".":
                    continue
                else:
                    if element not in arr:
                        arr.append(element)
                    else:
                        return False

        start = [[0, 0], [0, 3], [0, 6],
                [3, 0], [3, 3], [3, 6],
                [6, 0], [6, 3], [6, 6]]


        for i, j in start:
            arr = []
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    element = board[row][col]

                    if element == ".":
                        continue
                    else:
                        if element not in arr:
                            arr.append(element)
                        else:
                            return False

        return True 

        


        