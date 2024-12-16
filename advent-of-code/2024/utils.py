# Creates a list of the text of each line of the file
def readFile(filename):
    lines = []
    data = open(filename, 'r')
    
    while(1):
        line = data.readline()
        if line: lines.append(line.strip())
        else: return lines

# Converts list of strings to list of list of characters
def toGrid(grid):
    output = []
    for g in grid:
        thisRow = []
        for ch in g: thisRow.append(ch)
        output.append(thisRow)
    return output

# Prints grid
def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end="")
        print()