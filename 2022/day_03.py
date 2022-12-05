def priority(item):
	return (ord(item) - ord('a') + 1) if ('a' <= item <= 'z') else (ord(item) - ord('A') + 27)

file = open("input.txt", "r")
lines = file.read().split('\n')

rucksacks = map(lambda line: [line[0:(len(line)/2)], line[(len(line)/2):len(line)]], lines)
solutionPart1 = sum(map(priority, map(lambda item: list(item)[0], map(lambda rucksack: set(rucksack[0]) & set(rucksack[1]), rucksacks))))

rucksacksGroups = zip(lines[0::3], lines[1::3], lines[2::3])
solutionPart2 = sum(map(priority, map(lambda item: list(item)[0], map(lambda group: set(group[0]) & set(group[1]) & set(group[2]), rucksacksGroups))))

print(solutionPart1)
print(solutionPart2)
