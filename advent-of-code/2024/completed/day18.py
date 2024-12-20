# Importing useful function
from utils import readFile, printGrid

def part1(numBytes):
    def parseStr(s):
        vals = s.split("_")
        x, y = int(vals[0]), int(vals[1])
        return x, y

    data = readFile('inputs/day18.txt')

    grid = [['.' for i in range(71)] for j in range(71)]

    # Adding barriers to grid
    for i in range(numBytes):
        vals = data[i].split(',')
        x, y = int(vals[0]), int(vals[1])
        # print(x, y)
        grid[x][y] = "X"

    x, y = 0, 0

    # printGrid(grid)

    # Preparing bfs
    visited = set()
    visited.add(f"{x}_{y}")
    toVisit = set()
    toVisit.add(f"{x+1}_{y}")
    toVisit.add(f"{x}_{y+1}")
    steps = 0
    done = False

    # BFS
    while not done:
        # Getting this gen values
        thisVisit = list(toVisit)
        toVisit = set()
        steps += 1

        # Check for impossibility
        if len(thisVisit) == 0: return -1


        # Processing each node to visit
        for s in thisVisit:
            thisX, thisY = parseStr(s)
            
            if thisX < 0 or thisY < 0 or thisX > 70 or thisY > 70: continue # OOB
            if s in visited: continue # Already visited
            if grid[thisX][thisY] == "X": continue # Barrier
            if thisX == 70 and thisY == 70: # Destination
                done = True
                break

            # Adding neighboring cells to list to visit
            visited.add(f"{thisX}_{thisY}")
            toVisit.add(f"{thisX-1}_{thisY}")
            toVisit.add(f"{thisX+1}_{thisY}")
            toVisit.add(f"{thisX}_{thisY-1}")
            toVisit.add(f"{thisX}_{thisY+1}")

    # End of while

    return steps


def part2():

    def bs(minVal, maxVal, part1):
        while minVal < maxVal:
            mid = (minVal + maxVal) // 2
            if part1(mid) == -1:
                maxVal = mid
            else:
                minVal = mid + 1
        return minVal
    
    data = readFile('inputs/day18.txt')
    maxVal = len(data)
    minVal = 1024

    val = bs(minVal, maxVal, part1)
    return data[val-1]

    return 2

answer1 = part1(1024)
answer2 = part2()
print(answer1, answer2)
