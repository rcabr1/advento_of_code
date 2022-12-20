import re
import functools

def compare(left, right):
	if type(left) == int and type(right) == int:
		return (left > right) - (left < right)
	elif type(left) == int:
		return compare([left], right)
	elif type(right) == int:
		return compare(left, [right])

	for lElement, rElement in zip(left, right):
		compareElement = compare(lElement, rElement)
		if compareElement != 0:
			return compareElement

	return (len(left) > len(right)) - (len(left) < len(right))

fileRead = open('input.txt', 'r').read()
inputsPart1 = list(map(str.split, fileRead.split('\n\n')))

solutionPart1 = 0

for index, (left, right) in enumerate(inputsPart1):
	solutionPart1 += (index + 1) if compare(eval(left), eval(right)) < 0 else 0

inputsPart2 = list(map(eval, re.split(r'\n\n|\n',fileRead)))
inputsPart2.extend([[[2]], [[6]]])

sortedInputs = sorted(inputsPart2, key=functools.cmp_to_key(compare))
solutionPart2 = (sortedInputs.index([[2]]) +  1) * (sortedInputs.index([[6]]) + 1)

print(solutionPart1)
print(solutionPart2)
