import os
from functools import lru_cache

def FileFinder(address):
    path = os.getcwd() + address
    with open(path,'r') as file:
        bank = set(file.readline().rstrip().split(', '))
        towels = [x.rstrip() for x in file.readlines()][1:]
    return towels,bank

@lru_cache(None)
def Build(string,bank):
    if len(string) == 0:
        return 1
    total = 0
    i = 1
    while i <= len(string):
        if string[:i] in bank:
            add = Build(string[i:],bank)
            total += add
        i += 1
    return total

towels,bank = FileFinder("/Input data.txt")
total = 0
for towel in towels:
    print(towel)
    add = Build(towel,frozenset(bank))
    total += add
print(total)
