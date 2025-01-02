import os
import re

def FileFinder(address):
    locks = []
    keys = []
    path = os.getcwd()+address
    with open(path,'r') as file:
        text = file.read()
    schematics = [list(x.split('\n')) for x in text.split('\n\n')]
    for blueprints in schematics[:-1]:
        if blueprints[0][0] == '#':
            locks.append(blueprints)
        elif blueprints[0][0] == '.':
            keys.append(blueprints)
    return locks,keys

def Heights(blueprint):
    heights = [0,0,0,0,0]
    for i in range(len(blueprint[1:-1])):
        for j in range(len(blueprint[i])):
            if blueprint[i+1][j] == '#':
                heights[j] += 1
    return heights

def Fit(lock,key):
    for i in range(len(lock)):
        if key[i] + lock[i] > 5:
            return False
    return True

locks,keys = FileFinder("/Input data.txt")
locksH = [Heights(lock) for lock in locks]
keysH = [Heights(key) for key in keys]
total = 0
for lock in locksH:
    for key in keysH:
        if Fit(lock,key):
            total += 1
print(total)


