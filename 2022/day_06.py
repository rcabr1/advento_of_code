file = open("input.txt", "r")
content = file.read()

solutionPart1 = map(lambda index: len(set(content[index-4:index])) == 4, range(4, len(content))).index(True) + 4
solutionPart2 = map(lambda index: len(set(content[index-14:index])) == 14, range(14, len(content))).index(True) + 14

print(solutionPart1)
print(solutionPart2)
