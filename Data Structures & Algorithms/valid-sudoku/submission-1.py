class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 0 -> 0,1,2
        # 1 -> 3,4,5
        # 2 -> 6,7,8
        # 3 -> 0,1,2
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in s:
                        # print(s)
                        return False
                    else:
                        s.add(board[i][j])
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in s:
                        # print(s)
                        return False
                    else:
                        s.add(board[j][i])
        for k in range(9):
            s = set()
            a = (k//3)*3
            b = a+3
            # print(k,a,b)
            x = (k%3)*3
            y = x+3
            # print(k,x,y)
            for i in range(a,b):
                for j in range(x,y):
                    if board[i][j] != '.':
                        if board[i][j] in s:
                            return False
                        else:
                            s.add(board[i][j])
        return True

