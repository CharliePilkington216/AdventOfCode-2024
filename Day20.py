import os

def FileFinder(address):
    path = os.getcwd() + address
    with open(path,'r') as file:
        grid = [list(x.rstrip()) for x in file.readlines()]
    return grid

def EndStart(grid):
    start = None
    end = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                grid[i][j] = '0'
                start = (i,j)
            elif grid[i][j] == 'E':
                grid[i][j] = '.'
                end = (i,j)
            if start != None and end != None:
                return start,end
            
def Path(grid,start,end):
    num = 0
    vector = (-1,0)
    pos = start
    while pos != end:
        newPos = (pos[0]+vector[0],pos[1]+vector[1])
        if grid[newPos[0]][newPos[1]] == '.':
            num += 1
            pos = newPos
            grid[pos[0]][pos[1]] = str(num)
        else:
            vector = (-vector[1],vector[0])
    return grid

def Shortcut(grid,start,positions,cheats,timeTaken):
    num = int(grid[start[0]][start[1]])
    for pos in positions:
        if grid[pos[0]][pos[1]] != '#':
            num2 = int(grid[pos[0]][pos[1]])
            time = num-num2-timeTaken
            if time >= 100:
                try:
                    cheats[time] = cheats[time]+1
                except:
                    cheats[time] = 1
    return cheats

def Cheats(pos,time,limits,grid,cheats):
    positions = set()
    x = -time
    while x <= time:
        y = time-(abs(x))
        if pos[1]+x >= 0 and pos[1]+x < limits[1]:
            if pos[0]+y >= 0 and pos[0]+y < limits[0]:
                positions.add((pos[0]+y,pos[1]+x))
            if pos[0]-y >= 0 and pos[0]-y < limits[0]:
                positions.add((pos[0]-y,pos[1]+x))
        x += 1
    cheats = Shortcut(grid,pos,positions,cheats,time)
    return cheats

def nextPos(grid,pos,num):
    vector = (-1,0)
    found = False
    while not(found):
        newPos = (pos[0]+vector[0],pos[1]+vector[1])
        if newPos[0] >= 0 and newPos[0] < len(grid) and newPos[1] >= 0 and newPos[1] < len(grid[0]) and grid[newPos[0]][newPos[1]]!='#' and int(grid[newPos[0]][newPos[1]]) == num -1:
            return newPos,num-1
        vector = (-vector[1],vector[0])

grid = FileFinder("/Input data.txt")
start,end = EndStart(grid)
grid = Path(grid,start,end)
limits = (len(grid),len(grid[0]))
cheats = dict()
pos = end
num = int(grid[pos[0]][pos[1]])
while num > 100:
    for x in range(2,21):
        cheats = Cheats(pos,x,limits,grid,cheats)
    pos,num = nextPos(grid,pos,num)
total = 0
for cheat in cheats:
    total += cheats[cheat]
print(total)
