# Importing useful function
from utils import readFile, toGrid, printGrid

def part1():
    def isValid(lock, key):
        for i in range(5):
            if lock[i] + key[i] > 5: return False
        return True

    # Getting locks, grids
    data = readFile('inputs/day25.txt')
    locks = []
    keys = []
    for i in range(0, len(data), 8):
        grid = data[i:i+7]
        if grid[0] == "#####": # A lock
            heights = []
            for i in range(5):
                j = 1
                while grid[j][i] == "#": j += 1
                heights.append(j - 1)
            locks.append(heights)
        elif grid[0] == ".....": # A key
            heights = []
            for i in range(5):
                j = 5
                while grid[j][i] == "#": j -= 1
                heights.append(5 - j)
            keys.append(heights)

    # Checking all lock, key pairs
    count = 0
    for k in keys:
        for l in locks:
            if isValid(l, k): count += 1
    
    return count


def part2():
    data = readFile('inputs/day25.txt')

    return 2

answer1 = part1()
answer2 = part2()
print(answer1, answer2)