import os

def FileFinder(address):
    path = os.getcwd() + address
    with open(path,'r') as file:
        computers = dict()
        ports = dict()
        lines = list([])
        index = 0
        for x in file.readlines():
            line = x.rstrip().split('-')
            lines.append(line)
            if not(line[0] in computers):
                computers[line[0]] = index
                ports[index] = line[0]
                index += 1
            if not(line[1] in computers):
                computers[line[1]] = index
                ports[index] = line[1]
                index += 1
    return computers,ports,lines

def AdjMatrix(computers,lines):
    matrix = []
    for i in range(len(computers)):
        row = []
        for j in range(len(computers)):
            row.append(0)
        matrix.append(row)
    for line in lines:
        matrix[computers[line[0]]][computers[line[1]]] = 1
        matrix[computers[line[1]]][computers[line[0]]] = 1
    return matrix

computers,ports,lines = FileFinder("/Input data.txt")
matrix = AdjMatrix(computers,lines)
networks = set()
comp = 0
while comp < len(matrix):
    start = 0
    connections = matrix[comp]
    while 1 in connections[start:]:
        network = [ports[comp]]
        required = [comp]
        i = connections[start:].index(1) + start
        j = i
        while j < len(matrix):
            row = matrix[j]
            available = True
            for index in required:
                if row[index] == 0:
                    available = False
            if available:
                required.append(j)
                network.append(ports[j])
                networks.add(tuple(network))
            j += 1
        start = i + 1
    comp += 1
networks = list(networks)
networks = list({tuple(sorted(n)): None for n in networks}.keys())
networks = sorted([tuple(sorted(n)) for n in networks])
Max = len(networks[0])
for n in networks:
    if len(n) > Max:
        Max = len(n)
        result = n
output = ""
for comp in result:
    output += comp+","
print(output[:-1])
