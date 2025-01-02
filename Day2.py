import os

def FileFinder1(path):
    lines = []
    file = open(path,'r')
    text = file.readlines()
    for x in text:
        lines.append(x.rstrip())
    return lines

def Safe(nums,state):
    cases = 0
    i = 0
    while i < len(nums)-1:
        diff = int(nums[i]) - int(nums[i+1])
        if not((state == 1 and (diff < 0 and diff > -4)) or (state == 2 and (diff > 0 and diff < 4))) :
            try:
                diff = int(nums[i]) - int(nums[i+2])
                if not((state == 1 and (diff < 0 and diff > -4)) or (state == 2 and (diff > 0 and diff < 4))):
                    diff = int(nums[i + 1])-int(nums[i+2])
                    if i == 0 and ((state == 1 and (diff < 0 and diff > -4)) or (state == 2 and (diff > 0 and diff < 4))):
                        cases += 1
                    else:
                        return 0
                else:
                    cases += 1
                    i += 1
            except:
                cases += 1
        i += 1
    if cases < 2:
        return 1
    else:
        return 0
            

def Check(report):
    nums = report.split(' ')
    increase = 0
    decrease = 0
    i = 0
    while i < len(nums)-1:
        diff = int(nums[i])-int(nums[i+1])
        if diff > 0 and diff < 4:
            decrease += 1
        elif diff < 0 and diff > -4:
            increase += 1
        i +=1
    if increase > decrease:
        state = 1
    elif decrease > increase:
        state = 2
    else:
        return 0
    add = (Safe(nums,state))
    return add

address = "/Input data.txt"
path = os.getcwd() + address
reports = FileFinder1(path)
total = 0
for report in reports:
    total += Check(report)
print(total+1)
