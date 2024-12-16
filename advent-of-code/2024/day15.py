# Importing useful function
from utils import readFile, toGrid, printGrid

def part1():
    def scoreGrid(grid):
        score = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O": score += (100 * i + j)
        return score


    # Splitting data into grid and movements
    data = readFile('inputs/day15.txt')
    i = 0
    while data[i] != "": i += 1
    instructionsList = data[i+1:]
    data = data[:i]
    data = toGrid(data)

    # Joining instructions into one string
    instructions = "".join(instructionsList)
    # print(len(instructions))

    # Finding starting location
    x, y = 0, 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "@": 
                x = i
                y = j
                break
        if x != 0 or y != 0: break
    data[x][y] = "."

    # Attempting moves
    for move in instructions:

        # Case 1: up
        if move == "^": 
            if data[x-1][y] == "#": continue
            if data[x-1][y] == ".": 
                x -= 1
                continue

            # "O" above
            i = 1
            while data[x-i][y] == "O": i += 1
            if data[x-i][y] == ".": # Can move these blobs up
                data[x-i][y] = "O" # Putting blob in new spot
                data[x-1][y] = "." # Putting dot in new "me" spot
                x -= 1 # Moving my location

        # Case 2: down
        if move == "v": 
            if data[x+1][y] == "#": continue
            if data[x+1][y] == ".": 
                x += 1
                continue

            # "O" below
            i = 1
            while data[x+i][y] == "O": i += 1
            if data[x+i][y] == ".": # Can move these blobs down
                data[x+i][y] = "O" # Putting blob in new spot
                data[x+1][y] = "." # Putting dot in new "me" spot
                x += 1 # Moving my location
            
        # Case 3: left
        if move == "<": 
            if data[x][y-1] == "#": continue
            if data[x][y-1] == ".": 
                y -= 1
                continue

            # "O" left
            i = 1
            while data[x][y-i] == "O": i += 1
            if data[x][y-i] == ".": # Can move these blobs left
                data[x][y-i] = "O" # Putting blob in new spot
                data[x][y-1] = "." # Putting dot in new "me" spot
                y -= 1 # Moving my location

        # Case 4: right
        if move == ">": 
            if data[x][y+1] == "#": continue
            if data[x][y+1] == ".": 
                y += 1
                continue

            # "O" right
            i = 1
            while data[x][y+i] == "O": 
                i += 1
            if data[x][y+i] == ".": # Can move these blobs right
                data[x][y+i] = "O" # Putting blob in new spot
                data[x][y+1] = "." # Putting dot in new "me" spot
                y += 1 # Moving my location
    # End of iterating through moves
       
    # Calculating score
    score = scoreGrid(data)

    return score

def part2():
    def scoreGrid(grid):
        score = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O": score += (100 * i + j)
        return score


    # Splitting data into grid and movements
    data = readFile('inputs/day15.txt')
    i = 0
    while data[i] != "": i += 1
    instructionsList = data[i+1:]
    data = data[:i]
    data = toGrid(data)

    # Resizing grid
    grid = []
    for i in range(len(data)):
        newRow = []
        for j in range(len(data[i])):
            if data[i][j] == "#": 
                newRow.append("#")
                newRow.append("#")
            elif data[i][j] == "@":
                newRow.append("@")
                newRow.append(".")
            elif data[i][j] == ".":
                newRow.append(".")
                newRow.append(".")
            else:
                newRow.append("[")
                newRow.append("]")
        grid.append(newRow)
    data = grid
    # End of resizing

    # Joining instructions into one string
    instructions = "".join(instructionsList)

    # Finding starting location
    x, y = 0, 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "@": 
                x = i
                y = j
                break
        if x != 0 or y != 0: break
    data[x][y] = "."

    # Attempting moves
    for move in instructions:
        """TODO: BUG FIX"""
        """For horizontal moves, I only need to check that there's one free space at the side"""
        """But I would need to move every box by one space, meaning '[][].' becomes '.[][]. """
        """That involves updating every grid value en route"""

        """For vertical moves, I need to check if this box will push another box(es)"""
        """Each box could theoretically push more boxes each round"""
        """If ANY box doesn't have space to move it won't move"""
        """But if every box does have space to move, we need to again move every box, from furthest from start point to closest"""

        # Case 1: left
        if move == "<": 
            if data[x][y-1] == "#": continue
            if data[x][y-1] == ".": 
                y -= 1
                continue

            # "[]" left
            i = 1
            while data[x][y-i] == "]": i += 2
            if data[x][y-i] == "." and data[x][y-i-1] == ".": # Can move these blobs left
                data[x][y-i] = "]" # Putting blob in new spot
                data[x][y-i-1] = "[" # Putting blob in new spot
                data[x][y-1] = "." # Putting dot in new "me" spot
                data[x][y-2] = "." # Putting dot in new me spot
                y -= 1 # Moving my location

        # Case 4: right
        if move == ">": 
            if data[x][y+1] == "#": continue
            if data[x][y+1] == ".": 
                y += 1
                continue

            # "O" right
            i = 1
            while data[x][y+i] == "O": 
                i += 1
            if data[x][y+i] == ".": # Can move these blobs right
                data[x][y+i] = "O" # Putting blob in new spot
                data[x][y+1] = "." # Putting dot in new "me" spot
                y += 1 # Moving my location

    return 2

answer1 = part1()
answer2 = part2()
print(answer1, answer2)