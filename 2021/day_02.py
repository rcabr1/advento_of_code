file = open('input.txt', 'r')
lines = file.read().split('\n')

instructions = {'forward': (1,0), 'down': (0,1), 'up': (0,-1)}
horizontal, vertical, depthPart2 = 0, 0, 0

for line in lines:
	command, units = line.split(' ')
	vector = [int(units) * instruction for instruction in instructions[command]]
	horizontal, vertical, depthPart2 = horizontal+vector[0], vertical+vector[1], depthPart2+vector[0]*vertical

print(horizontal*vertical)
print(horizontal*depthPart2)
