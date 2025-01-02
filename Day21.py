import os
import re
from functools import cache

def FileFinder(address):
    path = os.getcwd() + address
    with open(path,'r') as file:
        codes = [x.rstrip() for x in file.readlines()]
    return codes

key = dict({'^':(0,1),
            '>':(1,2),
            'v':(1,1),
            '<':(1,0),
            'A':(0,2)})

def Valid(start,instructions,state):
    pos = start
    for char in instructions:
        if (pos == (3,0) and state == 1)or(pos == (0,0) and state == 2):
            return False
        match(char):
            case'^':
                pos = (pos[0]-1,pos[1])
                continue
            case'>':
                pos = (pos[0],pos[1]+1)
                continue
            case'v':
                pos = (pos[0]+1,pos[1])
                continue
            case'<':
                pos = (pos[0],pos[1]-1)
                continue
    return True

def Path(start,end,state):
    symboly = '^'
    symbolx = '<'
    diffy = start[0] - end[0]
    diffx = start[1] - end[1]
    if diffy < 0:
        symboly = 'v'
        diffy = -diffy
    if diffx < 0:
        symbolx = '>'
        diffx = -diffx
    instructions = (diffy*symboly+diffx*symbolx+'A',diffx*symbolx+diffy*symboly+'A')
    if Valid(start,instructions[0],state) and Valid(start,instructions[1],state) and instructions[0] != instructions[1]:
        return instructions
    elif Valid(start,instructions[0],state):
        return instructions[0]
    else:
        return instructions[1]

def KeyPad(start,code):
    output = ""
    for num in code:
        try:
            y = 3-(int(num)+2)//3
            if num != '0':
                x = (int(num)+2)%3
            else:
                x = 1
            cords = (y,x)
        except:
            cords = (3,2)
        string = Path(start,cords,1)
        start = cords
        if type(string) == tuple:
            T1 = Translate(string[0],19)
            T2 = Translate(string[1],19)
            output += Min(T1,T2)
        else:
            output += Translate(string,19)
    return output

def Min(string1,string2):
    if len(string1) > len(string2):
        return string2
    else:
        return string1

@cache
def Translate(string,depth):
    if depth == 0:
        return string
    output = ""
    subStrings = re.findall(r'.*A',string)
    for code in subStrings:
        pos = (0,2)
        for char in code:
            instructions = Path(pos,key[char],2)
            pos = key[char]
            if type(instructions) == tuple:
                T1 = Translate(instructions[0],depth-1)
                T2 = Translate(instructions[1],depth-1)
                output += Min(T1,T2)
            else:
                output += Translate(instructions,depth-1)
    return output

codes = FileFinder("/Input data.txt")
pos = (3,2)
total = 0
for code in codes:
    string = KeyPad(pos,code)
    print(len(string))
    complexity = int(re.findall(r'\d{1,3}',code)[0])*len(string)
    total += complexity
print(total)
