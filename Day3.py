import re
import os

def FileFinder(address):
    path = os.getcwd() + address
    with open(path,'r') as file:
        text = file.read()
    return text

def Part1(text):
    total = 0
    found = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)',text)
    for x in found:
        nums = [int(y) for y in re.findall(r'\d{1,3}',x)]
        total += nums[0]*nums[1]
    return total

def Part2(text):
    total = 0
    start = 0
    end = 0
    on = True
    while "do()" in text:
        if not(on):
            start = text.index("do()")
            on = True
        if "don't()" in text[start:]:
            end = text[start:].index("don't()")+start+1
        else:
            end = -1
        total += Part1(text[start:end])
        text = text[end:]
        on = False
    return total 

text = FileFinder("/Input data.txt")
p1 = Part1(text)
p2 = Part2(text)
print(p1)
print(p2)
