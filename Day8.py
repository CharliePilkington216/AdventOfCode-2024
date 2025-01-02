import os
import re

def FileFinder(path):
    file = open(path,'r')
    text = file.readlines()
    lines = [(x.rstrip()) for x in text]
    return lines

def FindAntiNodes(freq,lines,node,antinodes):
    locations = []
    for i in range(len(lines)):
        possible = True
        start = 0
        while possible:
            try:
                pos = lines[i][start:].index(freq)
                start = pos+1
                locations.append([int(i),int(pos)])
            except:
                possible = False
    for pos in locations:
        i = 0
        vector = [i*(pos[0]-node[0]),i*(pos[1]-node[1])]
        newPos = [(node[0]+vector[0]),(node[1]+vector[1])]
        while newPos[0] >= 0 and newPos[0] < len(lines) and newPos[1] >= 0 and newPos[1] < len(lines[0]) and pos != node:
            valid = True
            for position in antinodes:
                if position == newPos:
                    valid = False
            if valid:
                antinodes.append(newPos)
            i += 1
            vector = [i*(pos[0]-node[0]),i*(pos[1]-node[1])]
            newPos = [(node[0]+vector[0]),(node[1]+vector[1])]
    return antinodes

def Calc(lines):
    antinodes = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.':
                FindAntiNodes(lines[i][j],lines,[i,j],antinodes)
    return len(antinodes)      

address = "/Input data.txt"
path = os.getcwd() + address
lines = FileFinder(path)
output = Calc(lines)
print(output)
