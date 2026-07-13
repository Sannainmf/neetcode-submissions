class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            rows = []
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if not rows:
                        rows.append(board[i][j])
                    elif board[i][j] in rows:
                        return False
                    else:
                        rows.append(board[i][j])
                else:
                    continue

        for i in range(len(board)):
            cols = []
            for j in range(len(board[i])):
                if board[j][i] != ".":
                    if not cols:
                        cols.append(board[j][i])
                    elif board[j][i] in cols:
                        return False
                    else:
                        cols.append(board[j][i])
                else:
                    continue

        startNums = ([0,0], [3,0], [6,0],
                     [0,3], [3,3], [6,3],
                     [0,6], [3,6], [6,6])


        for i, j in startNums:
            final = []
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] != ".":
                        if not final:
                            final.append(board[row][col])
                        elif board[row][col] in final:
                            return False
                        else:
                            final.append(board[row][col])
                    else:
                        continue

        return True
