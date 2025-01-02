import os
from functools import cache

def FileFinder(address):
    path = os.getcwd() + address
    with open(path,'r') as file:
        nums = [x.rstrip() for x in file.readlines()]
    return nums

@cache
def Secret(num):
    binary = str(bin(num))[2:]
    binary += 6*'0'
    binary = str(bin(int(binary,2)^num))[2:]
    binary = binary[-24:]
    num = int(binary,2)

    binary = binary[:-5]
    binary = str(bin(int(binary,2)^num))[2:]
    binary = binary[-24:]
    num = int(binary,2)

    binary += 11*'0'
    binary = str(bin(int(binary,2)^num))[2:]
    binary = binary[-24:]

    return int(binary,2)

def Patterns(nums):
    patterns = dict()
    for num in nums:
        seen = set()
        changes = []
        prices = [int(str(num)[-1:])]
        for x in range(2000):
            num = Secret(int(num))
            prices.append(int(str(num)[-1:]))
            changes.append(prices[-1]-prices[-2])
            if len(changes)>4:
                key = tuple(changes[-4:])
                if not(key in seen):
                    try:
                        patterns[key] = patterns[key] + prices[-1]
                    except:
                        patterns[key] = prices[-1]
                seen.add(key)
    return patterns

nums = FileFinder("/Input data.txt")
sequences = Patterns(nums)
Max = 0
for pattern in sequences:
    if sequences[pattern] > Max:
        best = pattern
        Max = sequences[pattern]
print(best,Max)
