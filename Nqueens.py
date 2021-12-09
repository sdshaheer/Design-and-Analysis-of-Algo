def issafe(board,row,col):

    # checking coloumn
    for i in range(row,-1,-1):
        if board[i][col]==1:
            return False
    
    # checking left diagnol
    temprow=row
    tempcol=col
    while temprow>=0 and tempcol>=0:
        if board[temprow][tempcol]==1:
            return False
        temprow-=1
        tempcol-=1
    
    #checking right diagnol
    temprow=row
    tempcol=col
    while temprow>=0 and tempcol<len(board):
        if board[temprow][tempcol]==1:
            return False
        temprow-=1
        tempcol+=1

    return True

def find_queens(board,x):
    if x>=len(board):
        return True
    for i in range(len(board)):
        if issafe(board,x,i):
            board[x][i]=1
            if find_queens(board,x+1):
                return True
            else:
                board[x][i]=0
    return False

a=int(input("Enter size of board : "))
board=[[0 for j in range(a)] for i in range(a)]

if find_queens(board,0):
    for i in board:
        print(i)
else:
    print("No solution Exists")

    