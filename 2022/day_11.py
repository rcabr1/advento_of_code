class Monkey:
	def __init__(self, items, operation, test, sendTo):
		self.items = items
		self.operation = operation
		self.test = test
		self.sendTo = sendTo
		self.inspections = 0

file = open('input.txt', 'r')
monkeysEncoded = file.read().split('\n\n')

monkeyListPart1 = []
monkeyListPart2 = []

for monkeyEncoded in monkeysEncoded:
	monkeyLines = monkeyEncoded.split('\n')

	items = list(map(int, monkeyLines[1].split('Starting items: ')[1].split(', ')))
	operation = monkeyLines[2].split('Operation: new = ')[1].split(' ')
	test = int(monkeyLines[3].split('Test: divisible by ')[1])
	sendTo = list(map(lambda index: int(monkeyLines[index].split('throw to monkey ')[1]), range(4,6)))

	monkeyListPart1.append(Monkey(items.copy(), operation, test, sendTo))
	monkeyListPart2.append(Monkey(items.copy(), operation, test, sendTo))

# Parte 1
for turn in range(20):
	for monkey in monkeyListPart1:
		monkey.inspections += len(monkey.items)

		for item in monkey.items:
			operation = list(map(lambda element: item if element == 'old' else element, monkey.operation))

			if (operation[1] == '*'): worryLevel = (int(operation[0]) * int(operation[2])) // 3
			else: worryLevel = (int(operation[0]) + int(operation[2])) // 3

			monkeyListPart1[monkey.sendTo[not (worryLevel % monkey.test == 0)]].items.append(worryLevel)

		monkey.items = []

monkeyInspectionsPart1 = list(map(lambda monkey: monkey.inspections, monkeyListPart1))
monkeyInspectionsPart1.sort(reverse=True)

monkeyTestMultiplier = 1
for monkey in monkeyListPart2:
	monkeyTestMultiplier *= monkey.test

# Parte 2
for turn in range(10000):
	for monkey in monkeyListPart2:
		monkey.inspections += len(monkey.items)

		for item in monkey.items:
			operation = list(map(lambda element: item if element == 'old' else element, monkey.operation))

			if (operation[1] == '*'): worryLevel = (int(operation[0]) * int(operation[2])) % monkeyTestMultiplier
			else: worryLevel = (int(operation[0]) + int(operation[2])) % monkeyTestMultiplier

			monkeyListPart2[monkey.sendTo[not (worryLevel % monkey.test == 0)]].items.append(worryLevel)

		monkey.items = []

monkeyInspectionsPart2 = list(map(lambda monkey: monkey.inspections, monkeyListPart2))
monkeyInspectionsPart2.sort(reverse=True)

print(monkeyInspectionsPart1[0] * monkeyInspectionsPart1[1])
print(monkeyInspectionsPart2[0] * monkeyInspectionsPart2[1])
