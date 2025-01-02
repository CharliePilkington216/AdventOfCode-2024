import os

def FileFinder(address1,address2):
    path1 = os.getcwd()+ address1
    path2 = os.getcwd()+ address2
    file1 = open(path1,'r')
    file2 = open(path2,'r')
    grid = [x.rstrip() for x in file1.readlines()]
    instructions = file2.read().strip()
    return grid,instructions

def StartPos(grid):
    newGrid = []
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                pos =  [i,2*j]
                row += '@.'
            elif grid[i][j] == 'O':
                row += '[]'
            elif grid[i][j] == '.':
                row += '..'
            elif grid[i][j] == '#':
                row += '##'
        newGrid.append(row)
    return newGrid,pos

def Count(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '[':
                gps = i*100 + j
                total += gps
    return total

def Vector(char):
    match(char):
        case '^':
            return [-1,0]
        case '>':
            return [0,1]
        case 'v':
            return [1,0]
        case '<':
            return [0,-1]
        case _:
            return [0,0]

def NonComplex(pos,tempPos,vector,grid):
    y = tempPos[0]
    x = tempPos[1]
    while grid[y][x] == '[' or grid[y][x] == ']':
        y = y + vector[0]
        x = x + vector[1]
    if grid[y][x] == '.': 
        while [y,x] != pos:
            grid[y][x] = grid[y-vector[0]][x-vector[1]]
            y = y - vector[0]
            x = x - vector[1]
        grid[y][x] = '.'
        pos = tempPos
    return grid,pos

def Complex(tempPos,vector,grid):
    y = tempPos[0]
    x = tempPos[1]
    item = grid[y][x]
    if item == '[':
        doable = Complex([y+vector[0],x+vector[1]],vector,grid) and Complex([y+vector[0],x+vector[1]+1],vector,grid)
    elif item == ']':
        doable = Complex([y+vector[0],x+vector[1]],vector,grid) and Complex([y+vector[0],x+vector[1]-1],vector,grid)
    elif item != '#':
        return True
    else:
        return False
    return doable

def Move(tempPos,vector,grid):
    y = tempPos[0]
    x = tempPos[1]
    item = grid[y][x]
    if item == '[':
        grid = Move([y+vector[0],x+vector[1]],vector,grid)
        grid = Move([y+vector[0],x+vector[1]+1],vector,grid)
        grid[y][x] = grid[y-vector[0]][x-vector[1]]
        grid[y-vector[0]][x-vector[1]] = '.'
    elif item == ']':
        grid = Move([y+vector[0],x+vector[1]],vector,grid)
        grid = Move([y+vector[0],x+vector[1]-1],vector,grid)
        grid[y][x] = grid[y-vector[0]][x-vector[1]]
        grid[y-vector[0]][x-vector[1]] = '.'
    elif item != '#':
        grid[y][x] = grid[y-vector[0]][x - vector[1]]
        grid[y-vector[0]][x - vector[1]] = '.'
    return grid

def Simulate(grid,commands,pos):
    for move in commands:
        vector = Vector(move)
        tempPos = [pos[0] + vector[0],pos[1]+vector[1]]
        item = grid[tempPos[0]][tempPos[1]]
        if (item  == '[' or item == ']') and vector[0] != 0 :
            possible = Complex(tempPos,vector,grid)
            if possible:
                grid = Move(tempPos,vector,grid)
                grid[pos[0]][pos[1]] = '.'
                pos = tempPos
        elif item != '#':
            grid,pos = NonComplex(pos,tempPos,vector,grid)
    return grid

address1 = "/Grid.txt"
address2 = "/Instructions.txt"
grid,commands = FileFinder(address1,address2)
grid,pos = StartPos(grid)
grid = [list(x) for x in grid]
grid = Simulate(grid,commands,pos)
total = Count(grid)
print(total)
