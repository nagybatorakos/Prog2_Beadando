import numpy as np



board= np.array([['WR','WK','WB','WKing','WQ','WB','WK','WR'],
                 ['','WP','WP','WP','WP','WP','WP','WP'],
                 ['','','','','','','',''],
                 ['','','','','','','',''],
                 ['','','','','','','',''],
                 ['','','','','','','',''],
                 ['BP','BP','BP','BP','BP','BP','BP','BP'],
                 ['BR','BK','BB','BKing','BQ','BB','BK','BR']])

board_shape=board.shape

def getname(i ,j):
    return board[i][j]

# PositionOfPieces={'WR1':'0,0', 'WK1':'0,1','WB1':'0,2','WK':'0,3','WQ':'0,3','WB2','WK2','WR2'],
#                  ['WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8'}



from functools import partial


class Piece:
    def __init__(self,name):
        self.name=name



    def getPosition(self):
        for i in range(board_shape[0]):
            for j in range(board_shape[1]):
                if board[i][j] == self.name:
                    return str(i)+str(j)

class Rook(Piece):

    # pieces=['WR1','WR2','BR1','BR2']

    def __init__(self,name):
        Piece.__init__(self, name)
        self.name=name


    def canMove(self, i, j):
        possible_moves=[]
        char=self.name[0]
        #i,j= self.getPosition()

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

        for h in range(j+1, board_shape[1]):
            if h>7:
                break
            if board[i][h] != '' and board[i][h][0]==char:
                break
            possible_moves.append(str(i)+str(h))
            if board[i][h] != '' and board[i][h][0]!=char:
                break
        return possible_moves



class Knight(Piece):

    def __init__(self,name):
        Piece.__init__(self, name)

    def canMove(self, i, j):
        possible_moves=[]
        char=self.name[0]
        #i,j=self.getPosition()

        if i-2>=0 and j-1>=0:
            if board[i-2][j-1]=='' or board[i-2][j-1][0]!=char:
                possible_moves.append(str(i-2)+str(j-1))

        if i-1>=0 and j-2>=0:
            if board[i-1][j-2]=='' or board[i-1][j-2][0]!=char:
                possible_moves.append(str(i-1)+str(j-2))

        if i+1<8 and j-2>=0:
            if board[i+1][j-2]=='' or board[i+1][j-2][0]!=char:
                possible_moves.append(str(i+1)+str(j-2))

        if i+2<8 and j-1>=0:
            if board[i+2][j-1]=='' or board[i+2][j-1][0]!=char:
                possible_moves.append(str(i+2)+str(j-1))

        if i+2<8 and j+1<8:
            if board[i+2][j+1]=='' or board[i+2][j+1][0]!=char:
                possible_moves.append(str(i+2)+str(j+1))

        if i+1<8 and j+2<8:
            if board[i+1][j+2]=='' or board[i+1][j+2][0]!=char:
                possible_moves.append(str(i+1)+str(j+2))

        if i-2>=0 and j+1<8:
            if board[i-2][j+1]=='' or board[i-2][j+1][0]!=char:
                possible_moves.append(str(i-2)+str(j+1))

        if i-1>=0 and j+2<8:
            if board[i-1][j+2]=='' or board[i-1][j+2][0]!=char:
                possible_moves.append(str(i-1)+str(j+2))


        return possible_moves




class Bishop(Piece):

    def __init__(self,name):
        Piece.__init__(self,name)

    def canMove(self, i, j):
        possible_moves=[]
        char=self.name[0]
        #i,j=self.getPosition()

        if i+1<8 and j+1<8:
            h=j+1
            for v in range(i+1,board.shape[1]):

                if board[v][h]!='' and board[v][h][0]==char:
                    break
                possible_moves.append(str(v)+str(h))
                if board[v][h]!='' and board[v][h][0]!=char:
                    break
                h+=1
                if h==8:
                    break
            h=j

        if i-1>=0 and j+1<8:
            h=j+1
            for v in range(i-1,-1,-1):
                if board[v][h]!='' and board[v][h][0]==char:
                    break
                possible_moves.append(str(v)+str(h))
                if board[v][h]!='' and board[v][h][0]!=char:
                    break
                h+=1
                if h==8:
                    break
            h=j

        if i-1>=0 and j-1>=0:
            h=j-1
            for v in range(i-1,-1,-1):
                if board[v][h]!='' and board[v][h][0]==char:
                    break
                possible_moves.append(str(v)+str(h))
                if board[v][h]!='' and board[v][h][0]!=char:
                    break
                h-=1
                if h==-1:
                    break
            h=j

        if i+1<8 and j-1>=0:
            h=j-1
            for v in range(i+1,board.shape[1]):
                if board[v][h]!='' and board[v][h][0]==char:
                    break
                possible_moves.append(str(v)+str(h))
                if board[v][h]!='' and board[v][h][0]!=char:
                    break
                h-=1
                if h==-1:
                    break
            h=j
        return possible_moves




class King(Piece):
    def __init__(self,name):
        Piece.__init__(self,name)

    def canMove(self, i, j):
        possible_moves=[]
        char=self.name[0]
        #i,j=self.getPosition()
        if i-1>=0 and j-1>=0:
            if board[i-1][j-1]=='' or board[i-1][j-1][0]!=char:
                possible_moves.append(str(i-1)+str(j-1))

        if i-1>=0:
            if board[i-1][j]=='' or board[i-1][j][0]!=char:
                possible_moves.append(str(i-1)+str(j))

        if i-1>=0 and j+1<8:
            if board[i-1][j+1]=='' or board[i-1][j+1][0]!=char:
                possible_moves.append(str(i-1)+str(j+1))

        if j+1<8:
            if board[i][j+1]=='' or board[i][j+1][0]!=char:
                possible_moves.append(str(i)+str(j+1))

        if i+1<8 and j+1<8:
            if board[i+1][j+1]=='' or board[i+1][j+1][0]!=char:
                possible_moves.append(str(i+1)+str(j+1))

        if i+1<8 and j-1>=0:
            if board[i+1][j-1]=='' or board[i+1][j-1][0]!=char:
                possible_moves.append(str(i+1)+str(j-1))

        if i+1<8:
            if board[i+1][j]=='' or board[i+1][j][0]!=char:
                possible_moves.append(str(i+1)+str(j))

        if j-1>=0:
            if board[i][j-1]=='' or board[i][j-1][0]!=char:
                possible_moves.append(str(i)+str(j-1))

        # if len(possible_moves)>0:
        #     if char=='W':
        #         for i in possible_moves:
        #             for k in allB:
        #                 if i==k:
        #                     possible_moves.remove(i)
        #     elif char=='B':
        #         for i in possible_moves:
        #             for k in allW:
        #                 if i==k:
        #                     possible_moves.remove(i)

        return possible_moves


class Queen(Piece):
    def __init__(self,name):
        Piece.__init__(self,name)


    def canMove(self, i, j):
        possible_moves=[]
        char=self.name[0]
        #i,j=self.getPosition()

        if i+1<8 and j+1<8:
            h=j+1
            for v in range(i+1,board.shape[1]):
                if board[v][h]!='' and board[v][h][0]==char:
                    break
                possible_moves.append(str(v)+str(h))
                if board[v][h]!='' and board[v][h][0]!=char:
                    break
                h+=1
                if h==8:
                    break
            h=j

        if i-1>=0 and j+1<8:
            h=j+1
            for v in range(i-1,-1,-1):
                if board[v][h]!='' and board[v][h][0]==char:
                    break
                possible_moves.append(str(v)+str(h))
                if board[v][h]!='' and board[v][h][0]!=char:
                    break
                h+=1
                if h==8:
                    break
            h=j

        if i-1>=0 and j-1>=0:
            h=j-1
            for v in range(i-1,-1,-1):
                if board[v][h]!='' and board[v][h][0]==char:
                    break
                possible_moves.append(str(v)+str(h))
                if board[v][h]!='' and board[v][h][0]!=char:
                    break
                h-=1
                if h==-1:
                    break
            h=j

        if i+1<8 and j-1>=0:
            h=j-1
            for v in range(i+1,board.shape[1]):
                if board[v][h]!='' and board[v][h][0]==char:
                    break
                possible_moves.append(str(v)+str(h))
                if board[v][h]!='' and board[v][h][0]!=char:
                    break
                h-=1
                if h==-1:
                    break
            h=j

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

        for h in range(j+1, board_shape[1]):
            if h>7:
                break
            if board[i][h] != '' and board[i][h][0]==char:
                break
            possible_moves.append(str(i)+str(h))
            if board[i][h] != '' and board[i][h][0]!=char:
                break
        return possible_moves


class Pawn(Piece):
    def __init__(self,name):
        Piece.__init__(self,name)

    def canMove(self, i, j):
        possible_moves=[]
        char=self.name[0]
        #i,j=self.getPosition([0])
        # <>[]

        if char == 'W':
            if i==1 and board[i + 2][j] == '' and board[i+1][j]=='':
                possible_moves.append(str(i+2) + str(j))

            if i+1<8:
                if board[i+1][j]=='':
                    possible_moves.append(str(i+1)+str(j))

            if j-1>=0 and i+1<8 and board[i+1][j-1]!='' and board[i+1][j-1][0] =='B':
                possible_moves.append(str(i+1)+str(j-1))
            if j+1<8 and i+1<8 and board[i+1][j+1]!='' and board[i+1][j+1][0] =='B':
                possible_moves.append(str(i+1)+str(j+1))

        if char == 'B':
            if i ==6:
                if board[i - 2][j] == '' and board[i-1][j]=='':
                    possible_moves.append(str(i-2) + str(j))
            if i-1>=0:
                if board[i-1][j]=='':
                    possible_moves.append(str(i-1)+str(j))

            if j-1>=0 and board[i-1][j-1]!='' and board[i-1][j-1][0] =='W':
                possible_moves.append(str(i-1)+str(j-1))

            if j+1<8 and board[i-1][j+1]!='' and board[i-1][j+1][0] =='W':
                possible_moves.append(str(i-1)+str(j+1))

        return possible_moves


#
# c=Rook('BR1')
# #print(c.name)
# print(c.getPosition())
# print(c.canMove())
# b=Knight('BK1')
# #print(b.getName())
# print(b.getPosition())
# print(b.canMove())
# a=Bishop('WB1')
# print(a.getPosition())
# print(a.canMove())
# k=King('WK')
# print(k.getPosition())
# print((k.canMove()))

# q=Queen('BQ')
# print(q.getPosition())
# print(q.canMove())
