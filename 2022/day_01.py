import re

file = open("input.txt", "r")
fileContent = file.read()

elfSums = map(lambda elfSum: sum(map(int, elfSum.split("\n"))), fileContent.split("\n\n"))
elfSums.sort(reverse=True)

print(elfSums[0])
print(sum(elfSums[0:3]))
