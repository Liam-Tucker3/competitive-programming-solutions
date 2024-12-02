# Importing useful function
from utils import readFile

def part1():
    # Reading data
    data = readFile('inputs/day1.txt')
    l1, l2 = [], []
    for line in data:
        vals = line.split()
        l1.append(int(vals[0]))
        l2.append(int(vals[1]))

    # Sorting lists
    l1 = list(sorted(l1))
    l2 = list(sorted(l2))

    # Counting differences
    sumDiff = 0
    for i in range(len(l1)):
        v1, v2 = l1[i], l2[i]
        diff = v1 - v2
        if diff < 0: diff *= -1
        sumDiff += diff
    
    # Returning total difference
    return sumDiff

def part2():
    # Reading data
    data = readFile('inputs/day1.txt')
    l1, l2 = [], []
    for line in data:
        vals = line.split()
        l1.append(int(vals[0]))
        l2.append(int(vals[1]))

    # Calculating counts in list 2
    l2Counts = {}
    for v in l2:
        if v in l2Counts.keys(): l2Counts[v] += 1
        else: l2Counts[v] = 1
    
    # Calculating similarity score
    simScore = 0
    for v in l1:
        if v in l2Counts.keys(): simScore += v * l2Counts[v]
    
    # Return similarity score
    return simScore
    


answer1 = part1()
answer2 = part2()
print(answer1)
print(answer2)

    
        

    