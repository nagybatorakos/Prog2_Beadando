import numpy as np



board= np.array([['WR1','WK1','WB1','WQ','WK','WB2','WK2','WR2'],
                 ['WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8'],
                 ['','','','','','','',''],
                 ['','','','','','','',''],
                 ['','','','','','','',''],
                 ['','','','','','','',''],
                 ['BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8'],
                 ['BR1','BK1','BB1','BQ','BK','BB2','BK2','BR2']])

board_shape=board.shape

print(board.shape)


# PositionOfPieces={'WR1':'0,0', 'WK1':'0,1','WB1':'0,2','WK':'0,3','WQ':'0,3','WB2','WK2','WR2'],
#                  ['WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8'}


class Rook:

    # pieces=['WR1','WR2','BR1','BR2']

    def __init__(self, name):
        self.name = name

    def getPosition(self):
        for i in range(board_shape[0]):
            for j in range(board_shape[1]):
                if board[i][j] == self.name:
                    return i,j

    def canMove(self):
        possible_moves=[]
        char=self.name[0]
        i,j= self.getPosition()

        for v in range(i-1, -1,-1):
            if v<0:
                break
            if board[v][j] != '' and board[v][j][0]==char:
                break
            possible_moves.append(str(v)+str(j))
            if board[v][j] != '' and board[v][j][0]!=char:
                break

        for v in range(i+1, board_shape[0]):
            if v>7:
                break
            if board[v][j] != '' and board[v][j][0]==char:
                break
            possible_moves.append(str(v)+str(j))
            if board[v][j] != '' and board[v][j][0]!=char:
                break

        for h in range(j-1, -1,-1):
            if h<0:
                break
            if board[i][h] != '' and board[i][h][0]==char:
                break
            possible_moves.append(str(i)+str(h))
            if board[i][h] != '' and board[i][h][0]!=char:
                break

        for h in range(j+1, board_shape[0]):
            if h>7:
                break
            if board[i][h] != '' and board[i][h][0]==char:
                break
            possible_moves.append(str(i)+str(h))
            if board[i][h] != '' and board[i][h][0]!=char:
                break
        return possible_moves

c=Rook('BR1')
print(c.name)
print(c.getPosition())
print(c.canMove())
