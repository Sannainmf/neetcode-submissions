class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #each row contain digits 1-9
        for i in range(9):
            s = []
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                else:
                    if item != ".":
                        s.append(item)



        #each col contain digits 1-9

        for i in range(9):
            k = []
            for j in range(9):
                item = board[j][i]
                if item in k:
                    return False
                else:
                    if item != ".":
                        k.append(item)


        #each sub box contain digits 1-9

        starts = ([0,0], [0,3], [0,6],
                  [3,0], [3,3], [3,6],
                  [6,0], [6,3], [6,6])

        for i, j in starts:
            l = []
            for r in range(i, i+3):
                for c in range(j, j+3):
                    item = board[r][c]
                    if item in l:
                        return False
                    else:
                        if item != ".":
                            l.append(item)

        return True

        
        