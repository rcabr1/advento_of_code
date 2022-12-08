file = open('input.txt', 'r')
lines = file.read().split('\n')

m = [[int(value) for value in line] for line in lines]
R, C = len(m), len(m[0])

solPt1 = 0
for i in range(R):
	for j in range(C):
		x = m[i][j]
		solPt1 += all(m[r][j] < x for r in range(0, i)) or all(m[r][j] < x for r in range(i+1, R)) or all(m[i][c] < x for c in range(0, j)) or all(m[i][c] < x for c in range(j+1, C))

solPt2 = 0
for i in range(R):
	for j in range(C):
		solveUp, solveDown, solveLeft, solveRight = 0, 0, 0, 0
		x = m[i][j]
		for r in reversed(range(0, i)):
			solveUp += 1
			if m[r][j] >= x: break
		for r in range(i+1, R):
			solveDown += 1
			if m[r][j] >= x: break
		for c in reversed(range(0, j)):
			solveLeft += 1
			if m[i][c] >= x: break
		for c in range(j+1, C):
			solveRight += 1
			if m[i][c] >= x: break

		solPt2 = max(solPt2, solveUp * solveDown * solveLeft * solveRight)

print(solPt1)
print(solPt2)
