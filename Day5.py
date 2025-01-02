import os
import re

def FileFinder1(path):
    file = open(path,'r')
    text = file.read()
    text.strip()
    return text

def FileFinder2(path):
    lines = []
    file = open(path,'r')
    text = file.readlines()
    for x in text:
        lines.append(x.rstrip())
    return lines

def Check(arr,rules):
    i = 0
    while i < len(arr):
        element = arr[i]
        regex =  fr'{element}\|\d\d'
        instructions = re.findall(regex,rules)
        for rule in instructions:
            rule = rule.split('|')
            try:
                index = arr.index(rule[1])
                if index < i:
                    return False
            except:
                pass
        regex =  fr'\d\d\|{element}'
        instructions = re.findall(regex,rules)
        for rule in instructions:
            rule = rule.split('|')
            try: 
                index = arr.index(rule[0])
                if index >  i:
                    return False
            except:
                pass
        i+=1
    return True

def GetConns(arr,rules):
    conditions = set({})
    for element in arr:
        add1 = set(re.findall(fr'{element}\|\d\d',rules))
        add2 = set(re.findall(fr'\d\d\|{element}',rules))
        conditions = conditions|add1|add2
    return conditions

def Rearrange(arr,rules):
    if len(arr) == 1 or len(arr) == 0:
       return arr
    rules = list(rules)
    add1 = []
    add2 = []
    start = arr[0]
    before = re.findall(fr'\d\d\|{start}',str(rules))
    for x in before:
        nums =  x.split('|')
        if nums[0] in arr:
            add1.append(nums[0])
        rules.pop(rules.index(x))    
    after = re.findall(fr'{start}\|\d\d',str(rules))
    for x in after:
        nums = x.split('|')
        if nums[1] in arr:
            add2.append(nums[1])
        rules.pop(rules.index(x))
    return Rearrange(add1,rules) + list([arr[0]]) + Rearrange(add2,rules)
        
address1 = "/Input data.txt"
address2 = "/Lists.txt"
path = os.getcwd() + address1
rules = FileFinder1(path)
path = os.getcwd() + address2
checks = FileFinder2(path)
addup = []

for arr in checks:
    nums = arr.split(',')
    valid = Check(nums,rules)
    if not(valid):
        addup.append(nums)

new = []
for x in addup:
    conns = GetConns(x,rules)
    R = Rearrange(x,conns)
    new.append(R)

print(new)

total = 0
for L in new:
    total += int(L[len(L)//2])

print(total)

