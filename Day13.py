import math as maths
import os
import re

def FileFinder(address):
    path = os.getcwd() + address
    file = open(path,'r')
    lines = [x.rstrip() for x in file.readlines()]
    return lines
    
def ModulusArg(x,y):
    modulus = maths.sqrt((x**2)+(y**2))
    arg = maths.atan(y/x)
    return modulus,arg

def Effective(Vector,targetVector):
    angle = abs(Vector[1]-targetVector[1])
    dist = Vector[0]*maths.cos(angle)
    return dist

def Calculate(A,B,pos):
    cost = 0
    Apresses = 0
    Bpresses = 0
    VectorA = ModulusArg(A[0],A[1])
    VectorB = ModulusArg(B[0],B[1])
    while pos[0] > 0 and pos[1] > 0:
        targetVector = ModulusArg(pos[0],pos[1])
        Aeffective = Effective(VectorA,targetVector)
        Beffective = Effective(VectorB,targetVector)
        if Aeffective >= Beffective:
            Apresses += 1
            cost += 3
            pos = [pos[0]-A[0],pos[1]-A[1]]
        elif Beffective >= Aeffective:
            Bpresses += 1
            cost += 1
            pos = [pos[0]-B[0],pos[1]-B[1]]
    if Apresses <= 100 and Bpresses <= 100 and pos == [0,0]:
        return cost
    else:
        return 0

address = "/Input data.txt"
lines = FileFinder(address)
cost = 0
i = 0
while i < len(lines):
    A = [int(x) for x in re.findall(r'\d{1,100}',lines[i])]
    B = [int(x) for x in re.findall(r'\d{1,100}',lines[i+1])]
    pos = [int(x) for x in re.findall(r'\d{1,100}',lines[i+2])]
    cost += Calculate(A,B,pos)
    i += 4
print(cost)

    
