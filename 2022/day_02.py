file = open("input.txt", "r")
lines = file.read().split('\n')

pointsPart1 = ((4,8,3),(1,5,9),(7,2,6))
pointsPart2 = ((3,4,8),(1,5,9),(2,6,7))

parsedLines = map(lambda line: line.split(' '), lines)

solutionPart1 = sum(map(lambda line: pointsPart1[ord(line[0]) - ord('A')][ord(line[1]) - ord('X')], parsedLines))
solutionPart2 = sum(map(lambda line: pointsPart2[ord(line[0]) - ord('A')][ord(line[1]) - ord('X')], parsedLines))

print(solutionPart1)
print(solutionPart2)
