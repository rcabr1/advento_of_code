file = open('input.txt', 'r')
lines = list(map(list, file.read().split('\n')))

moves = [(0,1), (0,-1),(1,0), (-1,0)]

distPart1 = dict()
queuePart1 = []

distPart2 = dict()
queuePart2 = []

for row in range(len(lines)):
	for col in range(len(lines[0])):
		if lines[row][col] == 'S':
			start = (row,col)
			lines[row][col] = 'a'

			queuePart1.append(start)
			distPart1[start] = 0

			queuePart2.append(start)
			distPart2[start] = 0

		elif lines[row][col] == 'E':
			end = (row,col)
			lines[row][col] = 'z'

		elif lines[row][col] == 'a':
			queuePart2.append((row,col))
			distPart2[(row,col)] = 0

while (len(queuePart1) > 0):
	element = queuePart1[0]
	queuePart1 = queuePart1[1:]

	for move in moves:
		pos = (element[0]+move[0],element[1]+move[1])
		if 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0]):
			if pos not in distPart1 and ord(lines[pos[0]][pos[1]]) - ord(lines[element[0]][element[1]]) <= 1:
				distPart1[pos] = distPart1[element] + 1
				queuePart1.append(pos)

while (len(queuePart2) > 0):
	element = queuePart2[0]
	queuePart2 = queuePart2[1:]

	for move in moves:
		pos = (element[0]+move[0],element[1]+move[1])
		if 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0]):
			if pos not in distPart2 and ord(lines[pos[0]][pos[1]]) - ord(lines[element[0]][element[1]]) <= 1:
				distPart2[pos] = distPart2[element] + 1
				queuePart2.append(pos)

print(distPart1[end])
print(distPart2[end])
