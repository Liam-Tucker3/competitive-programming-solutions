# Importing useful function
from utils import readFile
import math

def part1():
    data = readFile('inputs/day8.txt')
    r, c, = len(data), len(data[0])

    # Getting all indices of antenna, sorted by category
    vals = {}
    for i in range(r):
        for j in range(c):
            ch = data[i][j]
            if ch == ".": continue # No antenna
            if ch in vals.keys(): vals[ch].append( (i, j) )
            else: vals[ch] = [(i, j)]

    # print(vals)
    
    # Considering each pair
    antinodes = set()
    for key in vals.keys():
        locs = vals[key]
        if len(locs) < 2: continue

        # Iterating through each pair of antennae
        for i in range(len(locs)):
            for j in range(i):
                x1, y1 = locs[i][0], locs[i][1]
                x2, y2 = locs[j][0], locs[j][1]

                # Two possible locations
                if (2*x2-x1) >= 0 and (2*x2-x1) < r and (2*y2-y1) >= 0 and (2*y2-y1) < c: antinodes.add(f"{2*x2-x1}_{2*y2-y1}")
                if (2*x1-x2) >= 0 and (2*x1-x2) < r and (2*y1-y2) >= 0 and (2*y1-y2) < c: antinodes.add(f"{2*x1-x2}_{2*y1-y2}")

                # print(f"({x1}, {y1}), ({x2}, {y2}) = ({2*x2-x1}, {2*y2-y1}), ({2*x1-x2}, {2*y1-y2})")

    # print(antinodes)
    return len(antinodes)

def part2():
    data = readFile('inputs/day8.txt')
    r, c, = len(data), len(data[0])

    # Getting all indices of antenna, sorted by category
    vals = {}
    for i in range(r):
        for j in range(c):
            ch = data[i][j]
            if ch == ".": continue # No antenna
            if ch in vals.keys(): vals[ch].append( (i, j) )
            else: vals[ch] = [(i, j)]

    # print(vals)
    
    # Considering each pair
    antinodes = set()
    for key in vals.keys():
        locs = vals[key]
        if len(locs) < 2: continue

        # Iterating through each pair of antennae
        for k in range(len(locs)): # Avoiding overwriting variable
            for j in range(k):
                x1, y1 = locs[k][0], locs[k][1]
                x2, y2 = locs[j][0], locs[j][1]
    
                # Adding this pair
                antinodes.add(f"{x2}_{y2}")
                antinodes.add(f"{x1}_{y1}")

                # Calculating difference
                dx, dy = x2-x1, y2-y1
                g = math.gcd(dx, dy)
                dx, dy = int(dx / g), int(dy/g)

                # Direction 1
                i = 1
                while (x2 + i*dx) >= 0 and (x2 + i*dx) < r and (y2 + i*dy) >= 0 and (y2 + i*dy) < c:
                    antinodes.add(f"{x2+i*dx}_{y2+i*dy}")
                    i += 1
                # Direction 2
                i = -1
                while (x2 + i*dx) >= 0 and (x2 + i*dx) < r and (y2 + i*dy) >= 0 and (y2 + i*dy) < c:
                    antinodes.add(f"{x2+i*dx}_{y2+i*dy}")
                    i -= 1

                # print(x1, y1, x2, y2)
                # print(antinodes)
                # print()

                # print(f"({x1}, {y1}), ({x2}, {y2}) = ({2*x2-x1}, {2*y2-y1}), ({2*x1-x2}, {2*y1-y2})")

    # print(antinodes)
    return len(antinodes)

answer1 = part1()
answer2 = part2()
print(answer1, answer2)