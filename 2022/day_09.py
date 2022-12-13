file = open('input.txt', 'r')
lines = file.read().split('\n')

tailTrackFirst, tailTrackLast = set(), set()
delta = {'R': (0,1), 'L': (0,-1), 'U': (1,0),  'D': (-1,0)}

head = [0,0]
rope = [[0,0] for _ in range(9)]

for line in lines:
	command, units = line.split(' ')

	for unit in range(int(units)):
		head = list(map(sum, zip(head, delta[command])))
		trackNext = head.copy()

		for x in range(9):
			if abs(rope[x][0] - trackNext[0]) > 1 or abs(rope[x][1] - trackNext[1]) > 1:
				rope[x][0] += (rope[x][0] < trackNext[0]) - (rope[x][0] > trackNext[0])
				rope[x][1] += (rope[x][1] < trackNext[1]) - (rope[x][1] > trackNext[1])
			trackNext = rope[x].copy()

		tailTrackFirst.add(tuple(rope[0]))
		tailTrackLast.add(tuple(rope[8]))

print(len(tailTrackFirst))
print(len(tailTrackLast))
