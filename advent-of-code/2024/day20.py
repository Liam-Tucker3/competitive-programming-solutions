# Importing useful function
from utils import readFile, toGrid, parseStr

def part1():
    def bfs(grid, x, y, targX, targY, maxX, maxY, verbose):
        # Creating already-visited set
        visited = set()
        visited.add(f"{x}_{y}")

        # Creating toVisit set
        toVisit = set()
        toVisit.add(f"{x+1}_{y}") # No need to check for OOB because start isn't along edge
        toVisit.add(f"{x}_{y+1}")
        toVisit.add(f"{x-1}_{y}")
        toVisit.add(f"{x}_{y+1}")
        steps = 0
        done = False

        # BFS
        while not done:
            # Getting this gen values
            thisVisit = list(toVisit)
            toVisit = set()
            steps += 1

            if verbose: print(steps, len(thisVisit), thisVisit)

            # Check for impossibility
            if len(thisVisit) == 0: return -1

            # Processing each node to visit
            for s in thisVisit:
                thisX, thisY = parseStr(s)
                
                if thisX < 0 or thisY < 0 or thisX >= maxX or thisY >= maxY: continue # OOB
                if s in visited: continue # Already visited
                if grid[thisX][thisY] == "#": continue # Barrier
                if thisX == targX and thisY == targY: # Destination
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
    # End of BFS function

    # Processing input
    data = readFile('inputs/day20.txt')
    data = toGrid(data)
    
    # Finding useful vars
    maxX = len(data)
    maxY = len(data[0])
    startX, startY, endX, endY = 0, 0, 0, 0
    for i in range(maxX):
        for j in range(maxY):
            if data[i][j] == "S":
                startX = i
                startY = j
                data[i][j] = "."
            elif data[i][j] == "E":
                endX = i
                endY = j
                data[i][j] = "."

    count = 0
    ps = bfs(data, startX, startY, endX, endY, maxX, maxY, verbose=False) # Length with no difference
    # print(ps)
    for i in range(maxX):
        for j in range(maxY):
            if data[i][j] != "#": continue # NO possible shortcut here
            
            # Calculating this shortcut time
            data[i][j] = "."
            thisPs = bfs(data, startX, startY, endX, endY, maxX, maxY, verbose = 0)
            data[i][j] = "#"
            # print(i, j, thisPs)
            if ps - thisPs >= 100: count += 1
            print(i, j, thisPs, ps)
            

    return count

def part2():
    data = readFile('inputs/day20.txt')

    return 2

answer1 = part1()
answer2 = part2()
print(answer1, answer2)