# Importing useful function
from utils import readFile, toGrid, printGrid, parseStrVar

def part1():
    grid = readFile('inputs/sample/day16.txt')
    grid = toGrid(grid)

    # Creating grid
    costs = [[[1000000000 for i in range(4)] for j in range(len(grid[0]))] for k in range(len(grid))]

    # Finding start, end values
    startX, startY, endX, endY = 0, 0, 0, 0
    maxX, maxY = len(grid), len(grid[0])
    for i in range(maxX):
        for j in range(maxY):
            if grid[i][j] == "E":
                grid[i][j] = "."
                endX = i
                endY = j
            if grid[i][j] == "S":
                grid[i][j] = "."
                startX = i
                startY = j
    
    # Preparing for bfs
    """Positions: N=0, E=1, S=2, W=3"""
    nextVisit = set()
    nextVisit.add(f"{startX}_{startY}_0")
    nextVisit.add(f"{startX}_{startY}_1")
    nextVisit.add(f"{startX}_{startY}_2")
    nextVisit.add(f"{startX}_{startY}_3")
    
    # Starting costs
    costs[startX][startY][3] = 0
    costs[startX][startY][0] = 1000
    costs[startX][startY][2] = 1000
    costs[startX][startY][1] = 2000

    # Modified BFS
    while len(nextVisit) > 0: 
        toVisit = list(nextVisit)
        nextVisit = set()
        for loc in toVisit:
            # Getting this indices
            vals = parseStrVar(loc, 3)
            x, y, d = vals[0], vals[1], vals[2]

            if grid[x][y] == "#": continue # Checking for OOB
            if x == endX and y == endY: continue # Checking for end

            # Adding new locations, if this is its new shortest path
            if costs[x][y][(d+1)%4] > costs[x][y][d] + 1000: # Turning right
                costs[x][y][(d+1)%4] = costs[x][y][d] + 1000
                nextVisit.add(f"{x}_{y}_{(d+1)%4}")
            if costs[x][y][(d-1)%4] > costs[x][y][d] + 1000: # Turning left
                costs[x][y][(d-1)%4] = costs[x][y][d] + 1000
                nextVisit.add(f"{x}_{y}_{(d-1)%4}")
            
            # Going straight
            if d == 0 and x-1 >= 0 and costs[x-1][y][d] > costs[x][y][d] + 1: # Up
                costs[x-1][y][d] = costs[x][y][d] + 1
                nextVisit.add(f"{x-1}_{y}_{d}")
            if d == 1 and y+1 < maxY and costs[x][y+1][d] > costs[x][y][d] + 1: # Right
                costs[x][y+1][d] = costs[x][y][d] + 1
                nextVisit.add(f"{x}_{y+1}_{d}")
            if d == 2 and x+1 < maxX and costs[x+1][y][d] > costs[x][y][d] + 1: # Down
                costs[x+1][y][d] = costs[x][y][d] + 1
                nextVisit.add(f"{x+1}_{y}_{d}")
            if d == 3 and y-1 >= 0 and costs[x][y-1][d] > costs[x][y][d] + 1: # Left
                costs[x][y-1][d] = costs[x][y][d] + 1
                nextVisit.add(f"{x}_{y-1}_{d}")
        
        # End of locations for this generation
        # toVisit = nextVisit

    # Outside of while loop

    finalCost = costs[endX][endY][0]
    for i in range(4): finalCost = min(finalCost, costs[endX][endY][i])

    return finalCost

def part2():
    grid = readFile('inputs/day16.txt')
    grid = toGrid(grid)

    # Creating grid
    costs = [[[[1000000000, set()] for i in range(4)] for j in range(len(grid[0]))] for k in range(len(grid))]

    # Finding start, end values
    startX, startY, endX, endY = 0, 0, 0, 0
    maxX, maxY = len(grid), len(grid[0])
    for i in range(maxX):
        for j in range(maxY):
            if grid[i][j] == "E":
                grid[i][j] = "."
                endX = i
                endY = j
            if grid[i][j] == "S":
                grid[i][j] = "."
                startX = i
                startY = j
    
    # Preparing for bfs
    nextVisit = set()
    nextVisit.add(f"{startX}_{startY}_0")
    nextVisit.add(f"{startX}_{startY}_1")
    nextVisit.add(f"{startX}_{startY}_2")
    nextVisit.add(f"{startX}_{startY}_3")
    
    # Starting costs, paths
    costs[startX][startY][3][0] = 0
    costs[startX][startY][0][0] = 1000
    costs[startX][startY][2][0] = 1000
    costs[startX][startY][1][0] = 2000
    
    # Only add start position to paths with valid initial costs
    for i in range(4):
        if costs[startX][startY][i][0] < 1000000000:
            costs[startX][startY][i][1].add(1000*startX + startY)

    # Modified BFS
    while len(nextVisit) > 0:
        toVisit = list(nextVisit)
        nextVisit = set()
        for loc in toVisit:
            vals = parseStrVar(loc, 3)
            x, y, d = vals[0], vals[1], vals[2]

            if grid[x][y] == "#": continue
            if x == endX and y == endY: continue

            # Turning right
            new_d = (d+1)%4
            new_cost = costs[x][y][d][0] + 1000
            if costs[x][y][new_d][0] >= new_cost:
                old_cost = costs[x][y][new_d][0]
                costs[x][y][new_d][0] = new_cost
                if old_cost > new_cost:
                    costs[x][y][new_d][1] = costs[x][y][d][1].copy()
                else:  # equal costs
                    costs[x][y][new_d][1] = costs[x][y][new_d][1] | costs[x][y][d][1]
                nextVisit.add(f"{x}_{y}_{new_d}")

            # Turning left
            new_d = (d-1)%4
            new_cost = costs[x][y][d][0] + 1000
            if costs[x][y][new_d][0] >= new_cost:
                old_cost = costs[x][y][new_d][0]
                costs[x][y][new_d][0] = new_cost
                if old_cost > new_cost:
                    costs[x][y][new_d][1] = costs[x][y][d][1].copy()
                else:  # equal costs
                    costs[x][y][new_d][1] = costs[x][y][new_d][1] | costs[x][y][d][1]
                nextVisit.add(f"{x}_{y}_{new_d}")

            # Moving straight
            if d == 0 and x-1 >= 0:  # Up
                new_cost = costs[x][y][d][0] + 1
                if costs[x-1][y][d][0] >= new_cost:
                    old_cost = costs[x-1][y][d][0]
                    costs[x-1][y][d][0] = new_cost
                    if old_cost > new_cost:
                        costs[x-1][y][d][1] = costs[x][y][d][1].copy()
                    else:  # equal costs
                        costs[x-1][y][d][1] = costs[x-1][y][d][1] | costs[x][y][d][1]
                    costs[x-1][y][d][1].add(1000*(x-1)+y)
                    nextVisit.add(f"{x-1}_{y}_{d}")

            if d == 1 and y+1 < maxY:  # Right
                new_cost = costs[x][y][d][0] + 1
                if costs[x][y+1][d][0] >= new_cost:
                    old_cost = costs[x][y+1][d][0]
                    costs[x][y+1][d][0] = new_cost
                    if old_cost > new_cost:
                        costs[x][y+1][d][1] = costs[x][y][d][1].copy()
                    else:  # equal costs
                        costs[x][y+1][d][1] = costs[x][y+1][d][1] | costs[x][y][d][1]
                    costs[x][y+1][d][1].add(1000*x+(y+1))
                    nextVisit.add(f"{x}_{y+1}_{d}")

            if d == 2 and x+1 < maxX:  # Down
                new_cost = costs[x][y][d][0] + 1
                if costs[x+1][y][d][0] >= new_cost:
                    old_cost = costs[x+1][y][d][0]
                    costs[x+1][y][d][0] = new_cost
                    if old_cost > new_cost:
                        costs[x+1][y][d][1] = costs[x][y][d][1].copy()
                    else:  # equal costs
                        costs[x+1][y][d][1] = costs[x+1][y][d][1] | costs[x][y][d][1]
                    costs[x+1][y][d][1].add(1000*(x+1)+y)
                    nextVisit.add(f"{x+1}_{y}_{d}")

            if d == 3 and y-1 >= 0:  # Left
                new_cost = costs[x][y][d][0] + 1
                if costs[x][y-1][d][0] >= new_cost:
                    old_cost = costs[x][y-1][d][0]
                    costs[x][y-1][d][0] = new_cost
                    if old_cost > new_cost:
                        costs[x][y-1][d][1] = costs[x][y][d][1].copy()
                    else:  # equal costs
                        costs[x][y-1][d][1] = costs[x][y-1][d][1] | costs[x][y][d][1]
                    costs[x][y-1][d][1].add(1000*x+(y-1))
                    nextVisit.add(f"{x}_{y-1}_{d}")

    # Finding best directions at end
    goodIndices = [0]
    for i in range(4):
        if costs[endX][endY][i][0] < costs[endX][endY][goodIndices[0]][0]:
            goodIndices = [i]
        elif costs[endX][endY][i][0] == costs[endX][endY][goodIndices[0]][0]:
            goodIndices.append(i)

    finalSet = set()
    for i in goodIndices:
        finalSet = finalSet | costs[endX][endY][i][1]
    
    finalSet.add(1000*endX + endY)
    return len(finalSet)

answer1 = part1()
answer2 = part2()
print(answer1, answer2)