import os
import re
import sys

sys.setrecursionlimit(100000)

def FileFinder(address):
    path = os.getcwd() + address
    file = open(path,'r')
    lines = [x.rstrip() for x in file.readlines()]
    return lines

def CreateGrid(limit):
    grid = []
    for i in range(limit):
        row = []
        for j in range(limit):
            row.append('.')
        grid.append(row)
    return grid

def TryPath(pos,vector,grid,cache):
    score = 1e15
    newPos = (pos[0] + vector[0],pos[1] + vector[1])
    if newPos[0] >= 0 and newPos [0] < len(grid) and newPos[1] >= 0 and newPos[1] < len(grid[0]) and grid[newPos[0]][newPos[1]] == '.':
        grid[pos[0]][pos[1]] = 'O'
        score,cache = Cache(newPos,vector,grid,cache)
        grid[pos[0]][pos[1]] = '.'
    return score,cache

def Pathing(pos,vector,grid,cache):
    if pos == (len(grid)-1,len(grid)-1):
        for x in grid:
            print(''.join(x))
        input()
        return 1,cache
    score = 1
    score1,cache = TryPath(pos,vector,grid,cache)
    vector = (vector[1],-vector[0])
    score2,cache = TryPath(pos,vector,grid,cache)
    vector = (-vector[0],-vector[1])
    score3,cache = TryPath(pos,vector,grid,cache)
    score += min(score1,score2,score3)
    return score,cache

def Cache(pos,vector,grid,cache):
    key = (pos[0],pos[1],vector[0],vector[1])
    if key in cache.keys():
        score,cache = Pathing(pos,vector,grid,cache)
        return score,cache
    else:
        score,cache = Pathing(pos,vector,grid,cache)
        cache[key] = score
        return score,cache

lines = FileFinder("/Input data.txt")
grid = CreateGrid(71)
for i in range(1024):
    x = lines[i]
    x,y = map(int,re.findall(r'\d{1,2}',x))
    grid[y][x] = '#'
for x in grid:
    print(''.join(x))
grid[0][0] = 'O'
cache = dict()
score,cache = Pathing((0,0),(0,1),grid,cache)
print(score-1)
