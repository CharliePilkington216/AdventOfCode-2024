import os
from itertools import product

def FileFinder(path):
    lines = []
    file = open(path,'r')
    text = file.readlines()
    for x in text:
        lines.append(x.rstrip())
    return lines

def Permutations(exponent):
    combinations = set(product([0, 1, 2], repeat=exponent))
    concatenated_combinations = {''.join(map(str, combo)) for combo in combinations}
    return concatenated_combinations

def Calc(lines):
    total = 0
    for line in lines:
        nums = line.split(' ')
        target = int(nums[0][:-1])
        nums = nums[1:]
        perms = list(Permutations(len(nums)-1))
        finished = False
        j = 0
        while j < len(perms) and not(finished):
            combo = perms[j]
            operation = int(nums[0])
            for i in range(len(combo)):
                if combo[i] == '0':
                    operation += int(nums[i+1])
                elif combo[i] == '1':
                    operation *= int(nums[i+1])
                elif combo[i] == '2':
                    operation = int(str(operation)+nums[i+1])
            if operation == target:
                total += target
                finished = True
            j += 1
    return total

address = "/Input data.txt"
path = os.getcwd()+address
lines = FileFinder(path)
total = Calc(lines)
print(total)
