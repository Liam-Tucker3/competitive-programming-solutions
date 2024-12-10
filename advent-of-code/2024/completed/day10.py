# Importing useful function
from utils import readFile

def part1():
    def parseStr(s):
        vals = s.split("_")
        # print(vals, s)
        return (int(vals[0]), int(vals[1]))

    data = readFile('inputs/day10.txt')
    r, c = len(data), len(data[0])

    trailheadScores = []
    for i in range(r):
        for j in range(c):
            if data[i][j] == "0": # Trailhead
                # Getting initial next locs
                thisSet = set()
                thisSet.add(f"{i}_{j}")

                for num in range(1, 10): # [1, 9]
                    # Tracking list of nodes to visit
                    thisList = list(thisSet)
                    nextSet = set()
                    for l in thisList:
                        thisX, thisY = parseStr(l)[0], parseStr(l)[1]

                        # Adding potential next vals
                        if thisX-1 >= 0 and int(data[thisX-1][thisY]) == num: nextSet.add(f"{thisX-1}_{thisY}")
                        if thisX+1 < r and int(data[thisX+1][thisY]) == num: nextSet.add(f"{thisX+1}_{thisY}")
                        if thisY-1 >= 0 and int(data[thisX][thisY-1]) == num: nextSet.add(f"{thisX}_{thisY-1}")
                        if thisY+1 < c and int(data[thisX][thisY+1]) == num: nextSet.add(f"{thisX}_{thisY+1}")
                    
                    if num == 9: 
                        trailheadScores.append(len(nextSet))
                    else: 
                        thisSet = nextSet
            # End if
        # End inner for
    # End outer for
    # print(trailheadScores)
    return sum(trailheadScores)

def part2():
    def parseStr(s):
        vals = s.split("_")
        # print(vals, s)
        return (int(vals[0]), int(vals[1]))

    def dfs(i, j, currVal, r, c, data):
        # Base case
        if currVal == 9: return 1

        # Other case
        count = 0
        if i-1 >= 0 and int(data[i-1][j]) == currVal + 1: count += dfs(i-1, j, currVal+1, r, c, data)
        if i+1 < r and int(data[i+1][j]) == currVal + 1: count += dfs(i+1, j, currVal+1, r, c, data)
        if j-1 >= 0 and int(data[i][j-1]) == currVal + 1: count += dfs(i, j-1, currVal+1, r, c, data)
        if j+1 < c and int(data[i][j+1]) == currVal + 1: count += dfs(i, j+1, currVal+1, r, c, data)

        return count

    data = readFile('inputs/day10.txt')
    r, c = len(data), len(data[0])

    trailheadScores = []
    for i in range(r):
        for j in range(c):
            if data[i][j] == "0": # Trailhead
                thisScore = dfs(i, j, 0, r, c, data)
                trailheadScores.append(thisScore)
               
            # End if
        # End inner for
    # End outer for
    # print(trailheadScores)
    return sum(trailheadScores)

answer1 = part1()
answer2 = part2()
print(answer1, answer2)