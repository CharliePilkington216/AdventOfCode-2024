import os

def FileFinder(path):
    file = open(path,'r')
    text = file.read().strip()
    return text

def Format(text):
    files = []
    file = ""
    ID = 0
    i = 0
    while i < len(text):
        if i % 2 == 0:
            file = []
            for j in range(int(text[i])):
                file .append(str(ID))
            files.append(file)
            ID += 1
        else:
            files.append(int(text[i]))
        i += 1
    return files

def IsInt(num):
    try:
        num +10
        return True
    except:
        return False

def Calc(files):
    end = len(files)-1
    while end > 0:
        if not(IsInt(files[end])):
            item = files[end]
            i = 0
            found = False
            while i < end and not(found):
                if IsInt(files[i]) and len(item) <= files[i]:
                    found = True
                    files[end-1] = files[end-1] + len(item)
                    if end +1 != len(files) and IsInt(files[end+1]):
                        files[end-1] = files[end-1] + files[end+1]
                        files.pop(end+1)
                    files.pop(end)
                    files[i] = files[i] - len(item)
                    files.insert(i,item)
                i += 1
            if not(found):
                end -= 1
        else:
            end -= 1
    total = 0
    index = 0
    for element in files:
        if IsInt(element):
            index += element
        else:
            for char in element:
                total += int(char) * index 
                index += 1                
    return total

address = "/Input data.txt"
path = os.getcwd() + address
text = FileFinder(path)
files =  Format(text)
output = Calc(files)
print(output)
