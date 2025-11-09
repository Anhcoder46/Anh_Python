inputList = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputList = []
index = 0

for i in range(len(inputList[0])):
    outputList.append([])
    for j in range(len(inputList)):
        outputList[index].append(inputList[j][index])
    index += 1
a, b, c = outputList[0], outputList[1], outputList[2]
print(a, b, c)