# Problem E
vals = input().split()
n = int(vals[0])
m = int(vals[1])

grid = []
for i in range(n):
    line = input()
    chs = []
    for l in line: chs.append(l)
    grid.append(chs)
    
for i in range(n):
    for j in range(m):
        grid[i][j] = [int(grid[i][j]), 10000000]
        
grid[0][0][1] = 0
        
next_indices = [(0, 0)]
sol = False

# print(len(grid), len(grid[0]))

while len(next_indices) > 0:
    thismove = next_indices[0]
    # print(thismove)
    if thismove[0] == n-1 and thismove[1] == m-1:
        sol=True
        break
    jsize = grid[thismove[0]][thismove[1]][0]
    # print(jsize)
    next_indices = next_indices[1:]
    if jsize == 0: continue
        
    if jsize <= thismove[0]:
        # print("A")
        oldLen = grid[thismove[0] - jsize][thismove[1]][1]
        newLen = grid[thismove[0]][thismove[1]][1] + 1
        if oldLen > newLen:
            grid[thismove[0] - jsize][thismove[1]][1] = newLen
            next_indices.append( (thismove[0] - jsize, thismove[1]))
            
    if jsize <= thismove[1]:
        # print("B")
        oldLen = grid[thismove[0]][thismove[1] - jsize][1]
        newLen = grid[thismove[0]][thismove[1]][1] + 1
        if oldLen > newLen:
            grid[thismove[0]][thismove[1] - jsize][1] = newLen
            next_indices.append( (thismove[0], thismove[1] - jsize))
            
    if thismove[0] + jsize < n:
        # print("C")
        oldLen = grid[thismove[0] + jsize][thismove[1]][1]
        newLen = grid[thismove[0]][thismove[1]][1] + 1
        if oldLen > newLen:
            grid[thismove[0] + jsize][thismove[1]][1] = newLen
            next_indices.append( (thismove[0] + jsize, thismove[1]))
    
    if jsize + thismove[1] < m:
        # print("D")
        oldLen = grid[thismove[0]][thismove[1] + jsize][1]
        newLen = grid[thismove[0]][thismove[1]][1] + 1
        if oldLen > newLen:
            grid[thismove[0]][thismove[1] + jsize][1] = newLen
            next_indices.append( (thismove[0], thismove[1] + jsize))
            
if sol: print(grid[n-1][m-1][1])
else: print("-1")
            