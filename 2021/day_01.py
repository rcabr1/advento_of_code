file = open("input.txt", "r")
fileList = map(int, file.readlines())

solutionPart1 = sum(map(lambda index: fileList[index] > fileList[index-1], range(1, len(fileList))))
solutionPart2 = sum(map(lambda index: fileList[index] > fileList[index-3], range(3, len(fileList))))

print(solutionPart1)
print(solutionPart2)
