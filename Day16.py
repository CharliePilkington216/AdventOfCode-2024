import os

def FileFinder(address):
    path = os.getcwd() + address
    file = open(path,'r')
    grid = [list(x.rstrip()) for x in file.readlines()]
    return grid

def StartEnd(grid):
    startPos = None
    endPos = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                startPos = [i,j]
            elif grid[i][j] == 'E':
                endPos = [i,j]
            elif startPos != None and endPos != None:
                return startPos,endPos
    return startPos,endPos
        
def Pathing(pos,endPos,vector,grid,visited):
    if pos == endPos:
        return 0
    visited.add(tuple(pos))
    score = 0
    check1 = [pos[0] + vector[1],pos[1]-vector[0]]
    check2 = [pos[0] - vector[1],pos[1]+vector[0]]
    check3 = [pos[0] + vector[0],pos[1]+vector[1]]
    path1 = 1e15
    path2 = 1e15
    path3 = 1e15
    if not(tuple(check1) in visited) and grid[check1[0]][check1[1]] != '#':
        path1 = Pathing(check1,endPos,[vector[1],-vector[0]],grid,visited.copy()) + 1001
    if not(tuple(check2) in visited) and grid[check2[0]][check2[1]] != '#':
        path2 = Pathing(check2,endPos,[-vector[1],vector[0]],grid,visited.copy()) + 1001
    if not(tuple(check3) in visited) and grid[check3[0]][check3[1]] != '#':
        path3 = Pathing(check3,endPos,vector,grid,visited.copy()) + 1
    score += min(path1,path2,path3)
    return score

address = "/Input data.txt"
grid = FileFinder(address)
start,end = StartEnd(grid)
visited = set()
score = Pathing(start,end,[0,1],grid,visited)
print(score)
