class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            s= []
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                else:
                    if item != ".":
                        s.append(item)

        for i in range(9):
            k= []
            for j in range(9):
                item = board[j][i]
                if item in k:
                    return False
                else:
                    if item != ".":
                        k.append(item)

        starts = ([0,0], [0,3], [0,6],
                  [3,0], [3,3], [3,6],
                  [6,0], [6,3], [6,6])

        for i, j in starts:
            l = []
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in l:
                        return False
                    else:
                        if item != ".":
                            l.append(item)


        return True

        