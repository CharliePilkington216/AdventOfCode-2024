import os
import re

def FileFinder(address):
    path = os.getcwd() + address
    with open(path,'r') as file:
        text = file.read()
    initiate = re.findall(r'.{3}: \d',text)
    operations = re.findall(r'.{11,12}->.{4}',text)
    return initiate,operations

def NOT(digit):
    if digit == 1:
        return 0
    elif digit == 0:
        return 1

def Calc(wires,eq):
    match(eq[1]):
        case "AND":
            return wires[eq[0]] & wires[eq[2]]
        case "OR":
            return wires[eq[0]] | wires[eq[2]]
        case "XOR":
            return (wires[eq[0]] | wires[eq[2]]) & (NOT(wires[eq[0]]) | NOT(wires[eq[2]]))

def Wires(init,operand):
    wires = dict()
    for data in init:
        data = data.split(': ')
        wires[data[0]] = int(data[1])
    i = 0
    while len(operand) != 0:
        if i == len(operand):
            i = 0
        equation = operand[i]
        LHS,RHS = equation.split(' -> ')
        LHS = LHS.split(' ')
        if LHS[0] in wires and LHS[2] in wires:
            wires[RHS] = Calc(wires,LHS)
            operand.pop(i)
        else:
            i += 1
    return wires

init,operand = FileFinder("/Input data.txt")
wires = Wires(init,operand)
z = 0
for wire in wires:
    if wire[0] == 'z' and wires[wire] == 1:
        z += 2 ** int(wire[1:])
print(z)
        
