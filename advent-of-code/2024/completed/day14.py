# Importing useful function
from utils import readFile

def part1():
    data = readFile('inputs/day14.txt')
    q1, q2, q3, q4 = 0, 0, 0, 0

    for line in data:
        # Getting first locations
        vals = line.split(' ')
        v1 = vals[0].split('=')[1].split(',')
        v2 = vals[1].split('=')[1].split(',')
        px, py = int(v1[0]), int(v1[1])
        vx, vy = int(v2[0]), int(v2[1])

        # Getting end location
        ex, ey = (px + 100 * vx) % 101, (py + 100 * vy) % 103

        # Getting quadrant
        if ex < 50 and ey < 51: q1 += 1
        elif ex < 50 and ey > 51: q2 += 1
        elif ex > 50 and ey < 51: q3 += 1
        elif ex > 50 and ey > 51: q4 += 1

    # Getting final score
    return (q1*q2*q3*q4)


def part2():
    def printGrid(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: print('.', end="")
                else: print("X", end="")
            print()

    data = readFile('inputs/day14.txt')

    # Creating grid
    # grid = [[0 for i in range(101)] for j in range(103)]

    # Loading values
    info = []

    # Getting data for each loc
    for line in data:
        # Getting first locations
        vals = line.split(' ')
        v1 = vals[0].split('=')[1].split(',')
        v2 = vals[1].split('=')[1].split(',')
        px, py = int(v1[0]), int(v1[1])
        vx, vy = int(v2[0]), int(v2[1])

        info.append( (px, py, vx, vy) )

    safetyFactors = []
    # Getting 100 generations with lowest safety factors
    """Using tip from AOC Reddit"""
    for s in range(101*103):
        q1, q2, q3, q4 = 0, 0, 0, 0

        # Calculating locations, adding to grid
        for i in range(len(info)):
            ex, ey = (info[i][0] + s * info[i][2]) % 101, (info[i][1] + s * info[i][3]) % 103

            # Getting quadrant
            if ex < 50 and ey < 51: q1 += 1
            elif ex < 50 and ey > 51: q2 += 1
            elif ex > 50 and ey < 51: q3 += 1
            elif ex > 50 and ey > 51: q4 += 1
        sf = q1*q2*q3*q4
        safetyFactors.append( (sf, s))

    # Printing 100 lowest safety factors to 
    safetyFactors = list(sorted(safetyFactors))
    for i in range(100):
        g = safetyFactors[i][1]

        # Creating grid
        grid = [[0 for i in range(103)] for j in range(101)]

        # Calculating locations, adding to grid
        for i in range(len(info)):
            ex, ey = (info[i][0] + g * info[i][2]) % 101, (info[i][1] + g * info[i][3]) % 103
            grid[ex][ey] += 1

        printGrid(grid)
        print(g)


    """
    # Simultating through
    seconds = 0
    while True:
        seconds -= 1

        # Creating grid
        grid = [[0 for i in range(103)] for j in range(101)]

        # Calculating locations, adding to grid
        for i in range(len(info)):
            ex, ey = (info[i][0] + seconds * info[i][2]) % 101, (info[i][1] + seconds * info[i][3]) % 103
            grid[ex][ey] += 1

        printGrid(grid)
        print(seconds)
        # val = input()
        # if val == "DONE": break
        if seconds == -1000: break

    return seconds
    """

answer1 = part1()
answer2 = part2()
print(answer1, answer2)