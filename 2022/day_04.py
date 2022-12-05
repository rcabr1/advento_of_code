import re

file = open("input.txt", "r")
lines = file.readlines()

containedPairs = 0
overlappedPairs = 0

for line in lines:
	ids = map(int, re.split(r',|-', line));

	containedPairs += (ids[0] - ids[2]) * (ids[1] - ids[3]) <= 0
	overlappedPairs += not (ids[0] > ids[3] or ids[1] < ids[2])

print(containedPairs)
print(overlappedPairs)
