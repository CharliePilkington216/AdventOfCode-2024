import os
import re

def FileFinder(address):
    path = os.getcwd() + address
    file = open(path,'r')
    text = file.read()
    registers = re.findall(r'Register .: \d{1,10}',text)
    file = open(path,'r')
    instructions = file.readlines()[-1].rstrip()
    return instructions,registers

def Ref(operand,registers):
    match(operand):
        case 4:
            return registers[0]
        case 5:
            return registers[1]
        case 6:
            return registers[2]
        case _:
            return operand

def Process(opcode,operand,literal,registers,i,num):
    match(opcode):
        case 0:
            registers[0] = registers[0]//(2**operand)
            return registers,i+2,num
        case 1:
            registers[1] = registers[1]^literal
            return registers,i+2,num
        case 2:
            registers[1] = operand%8
            return registers,i+2,num
        case 3:
            if registers[0] != 0:
                i = literal-2
            return registers,i+2,num
        case 4:
            registers[1] = registers[1]^registers[2]
            return registers,i+2,num
        case 5:
            num += f"{operand%8},"
            return registers,i+2,num
        case 6:
            registers[1] = registers[0]//(2**operand)
            return registers,i+2,num
        case 7:
            registers[2] = registers[0]//(2**operand)
            return registers,i+2,num
        case _:
            return registers,i+2,num

instructions,registers = FileFinder("/Input data.txt")
Input = re.findall(r'\d',instructions)
registers = list(map(int,re.findall(r'\d{1,10}',''.join(registers))))
i = 0
num = ""
while i < len(Input)-1:
    opcode = int(Input[i])
    operand = int(Input[i+1])
    literal = operand
    operand = Ref(operand,registers)
    registers,i,num = Process(opcode,operand,literal,registers,i,num)
    print(registers)
print(num)
