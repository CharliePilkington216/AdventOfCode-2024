import os

def FileFinder(path):
    lines = []
    file = open(path,'r')
    text = file.readlines()
    for x in text:
        lines.append(list(x.rstrip()))        
    return lines

def StartPos(board):
    i = 0
    while i < len(board):
        j = 0
        while j < len(board[i]):
            if board[i][j] == '^':
                return [i,j]
            j+=1
        i+=1

def Simulate(vector,board,pos):
    loops = 0
    y = pos[0] + vector[0]
    x = pos[1] + vector[1]
    while x>=0 and x< len(board[0]) and y>=0 and y < len(board):
        check = board[y][x]
        if check == '#':
            vector = [vector[1],(vector[0])*-1]
        elif check == ' · ':
            board,add = Block(vector,board,pos)
            loops += add
            pos = [y,x]
        else:
            pos = [y,x]
        y = pos[0] + vector[0]
        x = pos[1] + vector[1]
    return loops

def Block(vector,board,pos):
    analysis = False
    y = pos[0] + vector[0]
    x = pos[1] + vector[1]
    store = (y,x)
    board[y][x] = '#'
    visited = set({})
    while x>=0 and x< len(board[0]) and y>=0 and y < len(board):
        check = board[y][x]
        if check == '#':
            visited,loop = DetectLoop([y-vector[0],x-vector[1]],vector,visited)
            if loop:
                board[store[0]][store[1]] = ' 0'
                return board,1
            vector = [vector[1],(vector[0])*-1]
        else:
            pos = [y,x]
        y = pos[0] + vector[0]
        x = pos[1] + vector[1]
    board[store[0]][store[1]] = ' X'
    return board,0

def DetectLoop(pos,vector,visited):
    pos = str(pos[0])+str(pos[1])
    vector = str(vector[0])+str(vector[1])
    if pos+vector in visited:
        return visited,True
    else:
        visited.add(pos+vector)
        return visited,False

address = "/Input data.txt"
path = os.getcwd() + address
board = FileFinder(path)
vector = [-1,0]
for j in range(len(board)):
    for i in range(len(board[j])):
        if board[j][i] == '.':
            board[j][i] = ' · '
pos = StartPos(board)
board[pos[0]][pos[1]] = ' · '
loops = Simulate(vector,board,pos)
print(loops-1)
