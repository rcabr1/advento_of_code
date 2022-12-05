file = open("input.txt", "r")
content = file.read()

contentList = content.split("\n\n")

stackLines = contentList[0].split("\n")
stackContent = map(lambda stackLine: stackLine[1::4], stackLines)

stacksPart1 = map(lambda stack: filter(lambda element: element != ' ', stack[::-1]), map(list, zip(*stackContent)))
stacksPart2 = [list(stack) for stack in stacksPart1]

queryLines = contentList[1].split("\n")
queries = map(lambda queryLine: map(int, queryLine.split(" ")[1::2]), queryLines)

for query in queries:
	qMove, qFrom , qTo = [query[i] for i in range(3)]

	slicedPart1 = stacksPart1[qFrom-1][-qMove:][::-1]
	slicedPart2 = stacksPart2[qFrom-1][-qMove:]

	stacksPart1[qTo-1].extend(slicedPart1)
	stacksPart2[qTo-1].extend(slicedPart2)

	stacksPart1[qFrom-1] = stacksPart1[qFrom-1][:len(stacksPart1[qFrom-1])-qMove]
	stacksPart2[qFrom-1] = stacksPart2[qFrom-1][:len(stacksPart2[qFrom-1])-qMove]

print(''.join(map(lambda stack: stack[-1], stacksPart1)))
print(''.join(map(lambda stack: stack[-1], stacksPart2)))
