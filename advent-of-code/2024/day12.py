# Importing useful function
from utils import readFile

def part1():
    def getCost(points):
        perim = 4 * len(points)
        for i in range(len(points)):
            for j in range(len(points)):
                # Decreasing by one for shared edges
                if points[i][0] == points[j][0] and points[i][1] + 1 == points[j][1]: perim -= 1
                if points[i][0] == points[j][0] and points[i][1] - 1 == points[j][1]: perim -= 1
                if points[i][0] - 1 == points[j][0] and points[i][1] == points[j][1]: perim -= 1
                if points[i][0] + 1 == points[j][0] and points[i][1] == points[j][1]: perim -= 1
        return len(points) * perim # Area times perimeter
    
    def setToList(s):
        l = []
        for pair in s:
            vals = pair.split('_')
            l.append( (int(vals[0]), int(vals[1])) )
        return l
    
    def getSectors(grid):
        r, c = len(grid), len(grid[0])
        sectors = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == ".": continue # Avoiding double counting-- replacing already visited locations with dots

                thisCh = grid[i][j]
                thisRegion = set()
                thisRegion.add(f"{i}_{j}")

                # Modified BFS
                ops = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                while len(ops) != 0:
                    thisTuple = ops[0]
                    ops = ops[1:]
                    if thisTuple[0] < 0 or thisTuple[0] >= r or thisTuple[1] < 0 or thisTuple[1] >= c: continue # Index OOB
                    if f"{thisTuple[0]}_{thisTuple[1]}" in thisRegion: continue # Already in region
                    if grid[thisTuple[0]][thisTuple[1]] != thisCh: continue # Not part of this region

                    # Adding this cell to region
                    thisRegion.add(f"{thisTuple[0]}_{thisTuple[1]}")

                    # Adding neighbors
                    ops.append( (thisTuple[0]-1, thisTuple[1]) )
                    ops.append( (thisTuple[0]+1, thisTuple[1]) )
                    ops.append( (thisTuple[0], thisTuple[1]-1) )
                    ops.append( (thisTuple[0], thisTuple[1]+1) )
                # End while

                # Getting list of locs in this region
                thisRegionList = setToList(thisRegion)
                sectors.append(thisRegionList)

                # Dotting out this region
                for t in thisRegionList:
                    x, y = t[0], t[1]
                    grid[x][y] = "."

            # End inner for
        # End outer for
        return sectors
    
    grid = readFile('inputs/day12.txt')
    # Converting grid to list of lists
    for i in range(len(grid)):
        newGrid = []
        for j in range(len(grid[i])): newGrid.append(grid[i][j])
        grid[i] = newGrid

    # Getting sectors
    sectors = getSectors(grid)

    # Getting total cost
    cost = 0
    for s in sectors: cost += getCost(s)

    return cost

def part2():

    def getCost(points):
        sides = 0
        for p in points:
            # Calculating neighbors in shape
            neighbors = 0
            if (p[0]-1, p[1]) in points: neighbors += 1
            if (p[0]+1, p[1]) in points: neighbors += 1
            if (p[0], p[1]-1) in points: neighbors += 1
            if (p[0], p[1]+1) in points: neighbors += 1

            # Adding to sides as needed
            if neighbors == 0 or neighbors == 4: continue
            if neighbors == 3 or neigh
    
    def setToList(s):
        l = []
        for pair in s:
            vals = pair.split('_')
            l.append( (int(vals[0]), int(vals[1])) )
        return l
    
    def getSectors(grid):
        r, c = len(grid), len(grid[0])
        sectors = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == ".": continue # Avoiding double counting-- replacing already visited locations with dots

                thisCh = grid[i][j]
                thisRegion = set()
                thisRegion.add(f"{i}_{j}")

                # Modified BFS
                ops = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                while len(ops) != 0:
                    thisTuple = ops[0]
                    ops = ops[1:]
                    if thisTuple[0] < 0 or thisTuple[0] >= r or thisTuple[1] < 0 or thisTuple[1] >= c: continue # Index OOB
                    if f"{thisTuple[0]}_{thisTuple[1]}" in thisRegion: continue # Already in region
                    if grid[thisTuple[0]][thisTuple[1]] != thisCh: continue # Not part of this region

                    # Adding this cell to region
                    thisRegion.add(f"{thisTuple[0]}_{thisTuple[1]}")

                    # Adding neighbors
                    ops.append( (thisTuple[0]-1, thisTuple[1]) )
                    ops.append( (thisTuple[0]+1, thisTuple[1]) )
                    ops.append( (thisTuple[0], thisTuple[1]-1) )
                    ops.append( (thisTuple[0], thisTuple[1]+1) )
                # End while

                # Getting list of locs in this region
                thisRegionList = setToList(thisRegion)
                sectors.append(thisRegionList)

                # Dotting out this region
                for t in thisRegionList:
                    x, y = t[0], t[1]
                    grid[x][y] = "."

            # End inner for
        # End outer for
        return sectors
    
    grid = readFile('inputs/day12.txt')
    # Converting grid to list of lists
    for i in range(len(grid)):
        newGrid = []
        for j in range(len(grid[i])): newGrid.append(grid[i][j])
        grid[i] = newGrid

    # Getting sectors
    sectors = getSectors(grid)

    # Getting total cost
    cost = 0
    for s in sectors: cost += getCost(s)

    return cost

answer1 = part1()
answer2 = part2()
print(answer1, answer2)