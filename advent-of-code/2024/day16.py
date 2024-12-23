# Importing useful function
from utils import readFile, toGrid, printGrid, parseStrVar

def part1():
    grid = readFile('inputs/day16.txt')
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

    # print(costs[startX][startY][0], costs[startX-1][startY][0])

    # Modified BFS
    while len(nextVisit) > 0: 
        print("Part A Len:", len(nextVisit))
        toVisit = list(nextVisit)
        # print(toVisit)
        nextVisit = set()
        for loc in toVisit:
            # Getting this indices
            vals = parseStrVar(loc, 3)
            x, y, d = vals[0], vals[1], vals[2]
            # print(x, y, d, loc, vals)

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
            # if d == 0: print(d, x-1, costs[x-1][y][d], costs[x][y][d]+1)
            if d == 0 and x-1 >= 0 and costs[x-1][y][d] > costs[x][y][d] + 1: # Up
                costs[x-1][y][d] = costs[x][y][d] + 1
                nextVisit.add(f"{x-1}_{y}_{d}")
            if d == 1 and y-1 < maxY and costs[x][y+1][d] > costs[x][y][d] + 1: # Right
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
    print(maxX, maxY)
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
    
    # Starting costs, paths
    costs[startX][startY][3][0] = 0
    costs[startX][startY][0][0] = 1000
    costs[startX][startY][2][0] = 1000
    costs[startX][startY][1][0] = 2000
    for i in range(4): costs[startX][startY][i][1].add(1000*startX + startY)
    for i in range(4): print(costs[startX][startY][i][1])


    # print(costs[startX][startY][0], costs[startX-1][startY][0])

    # Modified BFS
    """TODO: Bug fix with representing indices in set"""
    while len(nextVisit) > 0: 
        print("LEN:", len(nextVisit))
        toVisit = list(nextVisit)
        # print(toVisit)
        nextVisit = set()
        for loc in toVisit:
            # Getting this indices
            vals = parseStrVar(loc, 3)
            x, y, d = vals[0], vals[1], vals[2]
            # print(x, y, d, loc, vals)

            if grid[x][y] == "#": continue # Checking for OOB
            if x == endX and y == endY: continue # Checking for end

            # Adding new locations, if this is its new shortest path
            if costs[x][y][(d+1)%4][0] >= costs[x][y][d][0] + 1000: # Turning right
                costs[x][y][(d+1)%4][0] = costs[x][y][d][0] + 1000
                nextVisit.add(f"{x}_{y}_{(d+1)%4}")
                if costs[x][y][(d+1)%4][0] > costs[x][y][d][0] + 1000: costs[x][y][(d+1)%4][1] = costs[x][y][d][1] # Case 1: Replace
                else: costs[x][y][(d+1)%4][1] = costs[x][y][d][1] | costs[x][y][(d+1)%4][1]

            if costs[x][y][(d-1)%4][0] >= costs[x][y][d][0] + 1000: # Turning left
                costs[x][y][(d-1)%4][0] = costs[x][y][d][0] + 1000
                nextVisit.add(f"{x}_{y}_{(d-1)%4}")
                if costs[x][y][(d-1)%4][0] > costs[x][y][d][0] + 1000: costs[x][y][(d+1)%4][1] = costs[x][y][d][1]
                else: costs[x][y][(d-1)%4][1] = costs[x][y][(d-1)%4][1] | costs[x][y][d][1]
            
            # Going straight
            # if d == 0: print(d, x-1, costs[x-1][y][d], costs[x][y][d]+1)
            if d == 0 and x-1 >= 0 and costs[x-1][y][d][0] >= costs[x][y][d][0] + 1: # Up
                costs[x-1][y][d][0] = costs[x][y][d][0] + 1
                nextVisit.add(f"{x-1}_{y}_{d}")
                if costs[x-1][y][d][0] > costs[x][y][d][0] + 1: costs[x-1][y][d][1] = costs[x][y][d][1]
                else: costs[x-1][y][d][1] = costs[x-1][y][d][1] | costs[x][y][d][1]
                costs[x-1][y][d][1].add(1000*(x-1)+y)

            if d == 1 and y+1 < maxY and costs[x][y+1][d][0] >= costs[x][y][d][0] + 1: # Right
                costs[x][y+1][d][0] = costs[x][y+1][d][0] + 1
                nextVisit.add(f"{x}_{y+1}_{d}")
                if costs[x][y+1][d][0] > costs[x][y][d][0] + 1: costs[x][y+1][d][1] = costs[x][y][d][1]
                else: costs[x][y+1][d][1] = costs[x][y+1][d][1] | costs[x][y][d][1]
                costs[x][y+1][d][1].add(1000*x+(y+1))

            if d == 2 and x+1 < maxX and costs[x+1][y][d][0] >= costs[x][y][d][0] + 1: # Down
                costs[x+1][y][d][0] = costs[x][y][d][0] + 1
                nextVisit.add(f"{x+1}_{y}_{d}")
                if costs[x+1][y][d][0] > costs[x][y][d][0] + 1: costs[x+1][y][d][1] = costs[x][y][d][1]
                else: costs[x+1][y][d][1] = costs[x+1][y][d][1] | costs[x][y][d][1]
                costs[x+1][y][d][1].add(1000*(x+1)+y)

            if d == 3 and y-1 >= 0 and costs[x][y-1][d][0] >= costs[x][y][d][0] + 1: # Left
                costs[x][y-1][d][0] = costs[x][y][d][0] + 1
                nextVisit.add(f"{x}_{y-1}_{d}")
                if costs[x][y-1][d][0] > costs[x][y][d][0] + 1: costs[x][y-1][d][1] = costs[x][y][d][1]
                else: costs[x][y-1][d][1] = costs[x][y-1][d][1] | costs[x][y][d][1]
                costs[x][y-1][d][1].add(1000*x+(y-1))
        
        # End of locations for this generation
        # toVisit = nextVisit

    # Outside of while loop

    # Getting all good spots
    goodIndices = [0]
    for i in range(4):
        if costs[endX][endY][i][0] < costs[endX][endY][goodIndices[0]][0]: goodIndices = [i]
        elif costs[endX][endY][i][0] == costs[endX][endY][goodIndices[0]][0]: goodIndices.append(i)

    finalSet = set() 
    for i in goodIndices: finalSet = finalSet | costs[endX][endY][i][1]
    print(goodIndices)
    for i in range(4): print(costs[endX][endY][i][1])
    return len(finalSet)

answer1 = part1()
answer2 = part2()
print(answer1, answer2)