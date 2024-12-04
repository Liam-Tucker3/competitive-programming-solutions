# Importing useful function
from utils import readFile

def part1():
    g = readFile('inputs/day4.txt')

    r = len(g)
    c = len(g[0])

    # Inefficient brute force
    count = 0
    for i in range(r):
        for j in range(c):
            if g[i][j] == "X": # Counting from X
                if i+3 < r: # DOWN
                    if g[i+1][j] == "M" and g[i+2][j] == "A" and g[i+3][j] == "S": count += 1
                if i+3 < r and j+3 < c: # DOWN RIGHT
                    if g[i+1][j+1] == "M" and g[i+2][j+2] == "A" and g[i+3][j+3] == "S": count += 1
                if j+3 < c: # RIGHT
                    if g[i][j+1] == "M" and g[i][j+2] == "A" and g[i][j+3] == "S": count += 1
                if i-3 >= 0 and j+3 < c: # UP RIGHT
                    if g[i-1][j+1] == "M" and g[i-2][j+2] == "A" and g[i-3][j+3] == "S": count += 1
                if i-3 >= 0: # UP
                    if g[i-1][j] == "M" and g[i-2][j] == "A" and g[i-3][j] == "S": count += 1
                if i-3 >= 0 and j-3 >= 0: # UP LEFT
                    if g[i-1][j-1] == "M" and g[i-2][j-2] == "A" and g[i-3][j-3] == "S": count += 1
                if j-3 >= 0: # LEFT
                    if g[i][j-1] == "M" and g[i][j-2] == "A" and g[i][j-3] == "S": count += 1
                if i+3 < r and j-3 >= 0: # DOWN LEFT
                    if g[i+1][j-1] == "M" and g[i+2][j-2] == "A" and g[i+3][j-3] == "S": count += 1
            # End if work if this char is "X"
    
    # End of iterating through grid
    return count

def part2():
    g = readFile('inputs/day4.txt')

    r = len(g)
    c = len(g[0])

    # Inefficient brute force
    count = 0
    for i in range(r):
        for j in range(c):
            if i-1 >= 0 and j-1 >= 0 and i+1 < r and j+1 < c and g[i][j] == "A": # Counting from A
                if g[i-1][j-1] == "M" and g[i+1][j+1] == "S" and g[i-1][j+1] == "M" and g[i+1][j-1] == "S": count += 1 # Case 1
                if g[i-1][j-1] == "M" and g[i+1][j+1] == "S" and g[i-1][j+1] == "S" and g[i+1][j-1] == "M": count += 1 # Case 2
                if g[i-1][j-1] == "S" and g[i+1][j+1] == "M" and g[i-1][j+1] == "M" and g[i+1][j-1] == "S": count += 1 # Case 3
                if g[i-1][j-1] == "S" and g[i+1][j+1] == "M" and g[i-1][j+1] == "S" and g[i+1][j-1] == "M": count += 1 # Case 4

    # End of iterating through grid
    return count

answer1 = part1()
answer2 = part2()
print(answer1, answer2)