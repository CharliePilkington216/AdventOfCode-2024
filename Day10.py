import os

def FileFinder(path):
    file = open(path,'r')
    text = file.readlines()
    lines = [list(x.rstrip()) for x in text]
    return lines

def FindPath(grid,height,pos,paths):
    vector = [-1,0]
    checked = 0
    while checked < 4:
        y = pos[0] + vector[0]
        x = pos[1] + vector[1]
        if y >=0 and y < len(grid) and x >= 0 and x < len(grid[y]):
            item = grid[y][x]
            if int(item) == 9 and int(item) == height +1:
                paths += 1
            elif int(item) == height + 1:
                paths = FindPath(grid,int(item),[y,x],paths)
        checked += 1
        vector = [vector[1],vector[0]*-1]
    return paths

address = "/Input data.txt"
path = os.getcwd() + address
grid = FileFinder(path)
total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if int(grid[i][j]) == 0:
            paths = FindPath(grid,0,[i,j],0)
            total += paths
print(total)
