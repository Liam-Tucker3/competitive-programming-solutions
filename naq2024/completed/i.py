# Light Up

n = int(input())
grid = []
for i in range(n): 
    vals = input()
    thisList = []
    for v in vals: thisList.append(v)
    grid.append(thisList)

# print(grid)

output = 1 # Successful
for i in range(n):
    for j in range(n):
        if grid[i][j] == "X": # Blocked cell, free
            continue

        validNeighbors = []
        if i != 0: validNeighbors.append( (i-1,j, 1) )
        if j != 0: validNeighbors.append( (i,j-1, 2) )
        if i+1 < n: validNeighbors.append( (i+1,j, 3) )
        if j+1 < n: validNeighbors.append( (i,j+1, 4) )

        if grid[i][j] == '.': # Open Cell
            okay = 0
            
            ti, tj = i, j
            while ti - 1 >= 0 and grid[ti-1][tj] == '.': ti -= 1
            if ti - 1 >= 0 and grid[ti-1][tj] == '?': okay = 1

            ti, tj = i, j
            while tj - 1 >= 0 and grid[ti][tj-1] == '.': tj -= 1
            if tj - 1 >= 0 and grid[ti][tj-1] == '?': okay = 1

            ti, tj = i, j
            while tj + 1 < n and grid[ti][tj+1] == '.': tj += 1
            if tj + 1 < n and grid[ti][tj+1] == '?': okay = 1

            ti, tj = i, j
            while ti + 1 < n and grid[ti+1][tj] == '.': ti += 1
            if ti + 1 < n and grid[ti+1][tj] == '?': okay = 1

            if not okay: 
                # print(i, j, grid[i][j])
                output = 0
                break

        elif grid[i][j] == '?': # Lightbulb

            okay = 1
            
            ti, tj = i, j
            while ti - 1 >= 0 and grid[ti-1][tj] == '.': ti -= 1
            if ti - 1 >= 0 and grid[ti-1][tj] == '?': okay = 0

            ti, tj = i, j
            while tj - 1 >= 0 and grid[ti][tj-1] == '.': tj -= 1
            if tj - 1 >= 0 and grid[ti][tj-1] == '?': okay = 0

            ti, tj = i, j
            while tj + 1 < n and grid[ti][tj+1] == '.': tj += 1
            if tj + 1 < n and grid[ti][tj+1] == '?': okay = 0

            ti, tj = i, j
            while ti + 1 < n and grid[ti+1][tj] == '.': ti += 1
            if ti + 1 < n and grid[ti+1][tj] == '?': okay = 0

            if not okay: 
                # print(i, j, grid[i][j])
                output = 0
                break
        
        else: # Blocked cell, specific number
            targetVal = int(grid[i][j])
            for t in validNeighbors:
                if grid[t[0]][t[1]] == '?': targetVal -= 1
            if targetVal != 0:
                # print(i, j, grid[i][j])
                output = 0
                break

    
    # End of j for loop
    if output == 0: break

print(output)
            
