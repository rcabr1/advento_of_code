file = open('input.txt', 'r')
lines = file.read().split('\n')

solutionPart1 = 0

delayMapper = {'noop': 1, 'addx': 2}
lineIndex, register, delay = 0, 1, 0
screen = []

for cycle in range(1, 240 + 1):
	if cycle in range(20, 240, 40): solutionPart1 += cycle * register

	screen.append('#' if ((cycle - 1) % 40) + 1 in range(register, register+3) else '.')

	delay += 1
	if delay == delayMapper[lines[lineIndex][:4]]:
		delay = 0
		if len(lines[lineIndex]) > 4: register += int(lines[lineIndex][5:])
		lineIndex += 1

solutionPart2 = '\n'.join(map(lambda line: ''.join(screen[line:line+40]), range(0, 240 + 1, 40)))

print(solutionPart1)
print(solutionPart2)
