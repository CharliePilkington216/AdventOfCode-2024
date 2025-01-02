import os

def FileFinder1(path):
    lines = []
    file = open(path,'r')
    text = file.readlines()
    for x in text:
        lines.append(x.rstrip())
    return lines

def FileFinder2(path):
    file = open(path,'r')
    text = file.read()
    return text

def Convert(lines):
    newLines = []
    for x in lines:
        newLines.append(int(x))
    return newLines

def Iterate1(row1,row2):
    total = 0
    count = 0
    for element in row1:
        count = 0
        for check in row2:
            if element == check:
                count += 1
        total += element*count
    print(total)

def Part1(row1,row2):
    total = 0
    for i in range(len(row1)):
        total += abs(row1[i]-row2[i])
    print(total)

def Sort(Input):
    row1 = []
    row2 = []
    for element in Input:
        data = element.split('   ')
        row1.append(int(data[0]))
        row2.append(int(data[1]))
    row1.sort()
    row2.sort()
    return row1,row2

address = "/Input data.txt"
path = os.getcwd() + address
Input = FileFinder1(path)
row1,row2 = Sort(Input)
Part1(row1,row2)
Iterate1(row1,row2)


