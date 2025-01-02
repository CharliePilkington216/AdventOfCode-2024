import os
import re

class Robot:
    def __init__(self,pos,vector,limits):
        self.pos = pos
        self.vector = vector
        self.limit = limits

    def Move(self,time):
        self.pos = [(self.pos[0]+(time*self.vector[0]))%self.limit[0],(self.pos[1]+(time*self.vector[1]))%self.limit[1]]

    def Quadrant(self):
        if self.pos[0] < self.limit[0]//2 and self.pos[1] < self.limit[1]//2:
            return 0
        elif self.pos[0] > self.limit[0]//2 and self.pos[1] < self.limit[1]//2:
            return 1
        elif self.pos[0] < self.limit[0]//2 and self.pos[1] > self.limit[1]//2:
            return 2
        elif self.pos[0] > self.limit[0]//2 and self.pos[1] > self.limit[1]//2:
            return 3
        else:
            return 4

def FileFinder(address):
    path = os.getcwd() + address
    file = open(path,'r')
    lines = [x.rstrip() for x in file.readlines()]
    return lines

def SetGrid(limit):
    grid = []
    for i in range(limit[1]):
        row = []
        for j in range(limit[0]):
            row.append(' ')
        grid.append(row)
    return grid

address = "/Input data.txt"
instructions = FileFinder(address)
limits = [101,103]
i = 0
quad = [0,0,0,0,0]
disorder = 100
while True:
    grid = SetGrid(limits)
    for line in instructions:
        settings = re.findall(r'\d{1,3}|-\d{1,3}',line)
        pos = [int(settings[0]),int(settings[1])]
        vector = [int(settings[2]),int(settings[3])]
        robo = Robot(pos,vector,limits)
        robo.Move(i)
        grid[robo.pos[1]][robo.pos[0]] = '.'
        quad[robo.Quadrant()] += 1
    disorder = abs(quad[0]-quad[1])+ abs(quad[2]-quad[3])
    i += 1
    if disorder < 50 or disorder > 350:
        print(f"{disorder} after {i-1} seconds")
        for x in grid:
            print(''.join(x))
