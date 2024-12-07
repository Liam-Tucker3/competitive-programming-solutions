# Importing useful function
from utils import readFile

def part1():
    data = readFile('inputs/day6.txt')
    r = len(data)
    c = len(data[0])

    # Getting initial location of guard
    i, j = 0, 0
    for x in range(r):
        for y in range(c):
            if data[x][y] == "^": 
                i = x
                j = y
                break

    # Simulating moving through grid
    dir = 0
    visitedLocs = set()
    while True:
        visitedLocs.add(f"{i}_{j}")
        if dir == 0: # Case 1: UP
            if i-1 >= 0:
                if data[i-1][j] == ".": i -= 1
                else: dir = (dir + 1) % 4
            else: break
        elif dir == 1: # Case 2: RIGHT
            if j+1 < c:
                if data[i][j+1] == ".": j += 1
                else: dir = (dir + 1) % 4
            else: break
        elif dir == 2: # Case 3: DOWN
            if i+1 < r:
                if data[i+1][j] == ".": i += 1
                else: dir = (dir + 1) % 4
            else: break
        else: # Case 4: LEFT
            if j-1 >= 0:
                if data[i][j-1] == ".": j -= 1
                else: dir = (dir + 1) % 4
            else: break

    return len(visitedLocs)

def part2():
    data = readFile('inputs/day6.txt')
    r = len(data)
    c = len(data[0])
    print(r)

    # Getting initial location of guard
    i, j = 0, 0
    for x in range(r):
        for y in range(c):
            if data[x][y] == "^": 
                i = x
                j = y
                break

    loopCount = 0
    iPerm, jPerm = i, j
    data[i] = data[i][:j] + "." + data[i][j+1:] # Replacing guards spot with open space
    # Iterating through indexes in the grid:
    for x in range(r):
        print(x)
        for y in range(c):
            if data[x][y] == ".":

                # Creating barrier
                data[x] = data[x][:y] + "#" + data[x][y+1:]
                i, j = iPerm, jPerm
                # print(x, y, i, j)

                # Simulating moving through grid, looking for loops
                dir = 0
                visitedLocs = set()
                while True:
                    # Checking for loop
                    if f"{i}_{j}_{dir}" in visitedLocs:
                        # print(x, y)
                        loopCount += 1
                        break

                    visitedLocs.add(f"{i}_{j}_{dir}")

                    # Moving thorugh grid
                    if dir == 0: # Case 1: UP
                        if i-1 >= 0:
                            if data[i-1][j] == ".": i -= 1
                            else: dir = (dir + 1) % 4
                        else: break
                    elif dir == 1: # Case 2: RIGHT
                        if j+1 < c:
                            if data[i][j+1] == ".": j += 1
                            else: dir = (dir + 1) % 4
                        else: break
                    elif dir == 2: # Case 3: DOWN
                        if i+1 < r:
                            if data[i+1][j] == ".": i += 1
                            else: dir = (dir + 1) % 4
                        else: break
                    else: # Case 4: LEFT
                        if j-1 >= 0:
                            if data[i][j-1] == ".": j -= 1
                            else: dir = (dir + 1) % 4
                        else: break

                # Returning to dot
                data[x] = data[x][:y] + "." + data[x][y+1:]
            # END IF
        # End inner for
    # End outer for

    # print(data)

    return loopCount

answer1 = part1()
answer2 = part2()
print(answer1, answer2)