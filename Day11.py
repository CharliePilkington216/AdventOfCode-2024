import os
from functools import cache

def Calc(num):
    if num == '0':
        return ['1']
    elif len(num)%2 == 0:
        return[num[:len(num)//2],str(int(num[len(num)//2:]))]
    else:
        return [str(int(num)*2024)]

@cache
def Solve(nums,depth):
    if depth >= 75:
        return len(nums)
    total = 0
    for num in nums:
        newNum = Calc(num)
        total += Solve(newNum,depth + 1)
    return total
            
def FileFinder(path):
    file = open(path,'r')
    stones = [x.rstrip() for x in file.read().split(' ')]
    return stones

address = "/Input data.txt"
path = os.getcwd() + address
stones = FileFinder(path)
total = Solve(stones,0)
print(total)
