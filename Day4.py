import os

def FileFinder(path):
    lines = []
    file = open(path,'r')
    text = file.readlines()
    for x in text:
        lines.append(x.rstrip())
    return lines

def Check(grid,cords,vector,depth):
    found = 0
    y = cords[0] - (2*vector[0])
    x = cords[1] - (2*vector[1])
    if y>=0 and y < len(grid) and x>=0 and x < len(grid[y]):
        if grid[y][x] == 'S':
            found += 1
    return found

def Surrounding(cords,grid):
    PrevXY = []
    mnum = 0
    snum = 0
    found = 0
    for i in range(-1,2,2):
        for j in range(-1,2,2):
            y = cords[0] + i
            x = cords[1] + j
            if y>=0 and y < len(grid) and x>=0 and x < len(grid[y]):
                if grid[y][x] == 'M' and mnum == 0:
                    PrevXY = [y,x]
                    mnum += 1
                elif grid[y][x] == 'M':
                    if y != PrevXY[0] and x != PrevXY[1]:
                        return 0
                    mnum +=1
                elif grid[y][x] == 'S':
                    snum += 1
    if mnum == snum and snum == 2 and mnum == 2:
        return 1
    else:
        return 0
                

def WordSearch(grid):
    total = 0
    i = 1
    while i < len(grid)-1:
        j = 1
        while j < len(grid[i])-1:
            element = grid[i][j]
            if element == 'A':
                calc = Surrounding([i,j],grid)
                total   += calc
            j += 1
        i += 1
    return total

if __name__ == "__main__":
    address = "/Input data.txt"
    path = os.getcwd() + address
    grid = FileFinder(path)
    output = WordSearch(grid)
    print(output)
