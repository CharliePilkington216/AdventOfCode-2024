import os

def FileFinder(path):
    file = open(path,'r')
    text = file.readlines()
    grid = [list(x.rstrip()) for x in text]
    return grid

def Fence(grid,prevVector,pos,area,visited):
    vector = [-1,0]
    search = grid[pos[0]][pos[1]]
    counter = 0
    while counter < 4:
        y = pos[0]+vector[0]
        x = pos[1]+vector[1]
        if y >=0 and y < len(grid) and x >= 0 and x < len(grid[y]):
            if vector != prevVector and not((y,x)in visited):
                if grid[y][x] == search:
                    area += 1
                    visited.add((y,x))
                    area,visited = Fence(grid,[vector[0]*-1,vector[1]*-1],[y,x],area,visited)
        else:
            cord = tuple((pos[0] + vector[0], pos[1] + vector[1]))
        vector = [vector[1],vector[0]*-1]
        counter += 1
    return area,visited

def Sides(visited):
    points = list([])
    for block in visited:
        if not((block[0]-1,block[1])in visited):
            if not((block[0],block[1]-1)in visited):
               points.append(block)
            if not((block[0],block[1]+1)in visited):
                points.append((block[0],block[1]+1))
        if not((block[0]+1,block[1])in visited):
            if not((block[0],block[1]-1)in visited):
               points.append((block[0]+1,block[1]))
            if not((block[0],block[1]+1)in visited):
                points.append((block[0]+1,block[1]+1))
    for block in visited:
        if not((block[0]-1,block[1]-1)in visited) and (block[0]-1,block[1])in visited and (block[0],block[1]-1)in visited:
            points.append(block)
        if not((block[0]-1,block[1]+1)in visited) and (block[0]-1,block[1])in visited and (block[0],block[1]+1)in visited:
            points.append((block[0],block[1]+1))
        if not((block[0]+1,block[1]-1)in visited) and (block[0]+1,block[1])in visited and (block[0],block[1]-1)in visited:
            points.append((block[0],block[1]+1))
        if not((block[0]+1,block[1]+1)in visited) and (block[0]+1,block[1])in visited and (block[0],block[1]+1)in visited:
            points.append((block[0]+1,block[1]+1))
    return points
    
address = "/Input data.txt"
path = os.getcwd() + address
grid = FileFinder(path)
seen = set({})
total = 0
i = 0
while i < len(grid):
    j = 0
    while j < len(grid[i]):
        pos = (i,j)
        if not(pos in seen):
            visited = set({pos})
            area,visited = Fence(grid,[0,0],pos,1,visited)
            points = Sides(visited)
            total += area*len(points)
            seen = seen | visited
        j += 1
    i += 1
print(total)
