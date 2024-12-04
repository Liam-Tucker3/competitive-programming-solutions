# Importing useful function
from utils import readFile

def part1():
    # Reading data
    data = readFile('inputs/day2.txt')

    # Iterating through data
    safeCount = 0
    for line in data:
        vals = line.split()
        for i in range(len(vals)): vals[i] = int(vals[i]) # Converting vals to int
        for i in range(1, len(vals)): vals[i-1] = vals[i] - vals[i-1] # Calculating differences
        vals = vals[:len(vals) - 1] # removing last value

        # Checking if safe
        if min(vals) >= 1 and max(vals) <= 3: safeCount += 1
        if min(vals) >= -3 and max(vals) <= -1: safeCount += 1
    
    return safeCount

# Very inefficient solution
def part2():
    data = readFile('inputs/day2.txt')

    # Iterating through data
    safeCount = 0
    for line in data:
        vals = line.split()
        for i in range(len(vals)): vals[i] = int(vals[i]) # Converting vals to int

        thisCount = 0
        for i in range(len(vals)): # Iterating through individual elements to try removing
            temp = vals[:i] + vals[i+1:] 
            for j in range(1, len(temp)): temp[j-1] = temp[j] - temp[j-1] # Calculating differences
            temp = temp[:len(temp)-1] # Removing last value

            # Checking if safe
            if min(temp) >= 1 and max(temp) <= 3: thisCount = 1
            if min(temp) >= -3 and max(temp) <= -1: thisCount = 1

            # Early return
            if thisCount > 0: break

        safeCount += thisCount # Incrementing
    
    return safeCount

answer1 = part1()
answer2 = part2()
print(answer1, answer2)