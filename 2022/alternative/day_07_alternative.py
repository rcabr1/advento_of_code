class File:
	def __init__(self, name, size):
		self.name = name
		self.size = size

class Directory:
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.listFiles = []
		self.listSubdirectories = []

	def getSubdirectory(self, directoryName):
		return filter(lambda directory: directory.name == directoryName, self.listSubdirectories)[0]

	def getSize(self):
		return sum(map(lambda file: file.size, self.listFiles)) + sum(map(lambda directory: directory.getSize(), self.listSubdirectories))

	def sumSmallDirectories(self):
		directorySize = self.getSize()
		return directorySize * (directorySize < 100000) + sum(map(lambda directory: directory.sumSmallDirectories(), self.listSubdirectories))

	def closerBigDirectory(self, totalSize):
		directorySize = self.getSize()
		if totalSize - directorySize > 40000000: return totalSize
		return min(directorySize, min(map(lambda directory: directory.closerBigDirectory(totalSize), self.listSubdirectories)))

class Terminal:
	def __init__(self, rootName):
		self.root = Directory(rootName, '')
		self.currentDirectory = self.root

	def goTo(self, directoryName):
		if (directoryName == '..'): self.currentDirectory = self.currentDirectory.parent
		else: self.currentDirectory = self.currentDirectory.getSubdirectory(directoryName)

	def addListElement(self, element):
		if (element[0] == 'dir'): self.currentDirectory.listSubdirectories.append(Directory(element[1], self.currentDirectory))
		else: self.currentDirectory.listFiles.append(File(element[1], int(element[0])))

	def sumSmallDirectories(self):
		return self.root.sumSmallDirectories()

	def closerBigDirectory(self):
		return self.root.closerBigDirectory(self.root.getSize())

file = open('input.txt', 'r')
lines = file.read().split('\n')

terminal = Terminal(lines[0].split(' ')[2])

index = 1
while index < len(lines):
	command = lines[index].split(' ')

	if command[1] == 'ls':
		while index+1 < len(lines):
			listElement = lines[index+1].split(' ')
			
			if listElement[0] == '$': break
			else: terminal.addListElement(listElement)

			index += 1
	else:
		terminal.goTo(command[2])

	index += 1

print(terminal.sumSmallDirectories())
print(terminal.closerBigDirectory())
