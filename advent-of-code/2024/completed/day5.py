# Importing useful function
from utils import readFile

def part1():
    data = readFile('inputs/day5.txt')

    # Splitting data into rules and jobs
    rules = []
    jobs = []
    beforeLine = True
    for line in data:
        if line == "": beforeLine = False
        elif beforeLine: rules.append(line)
        else: jobs.append(line)

    # Getting list of dependencies
    beforeList = {} # Keys are jobs, values are jobs they have to be before
    for r in rules:
        vals = r.split('|')
        if int(vals[0]) in beforeList.keys(): beforeList[int(vals[0])].append(int(vals[1]))
        else: beforeList[int(vals[0])] = [int(vals[1])]

    # Iterating through lists of jobs
    midNums = 0
    for l in jobs:
        # Processing input
        vals = l.split(',')
        for i in range(len(vals)): vals[i] = int(vals[i])

        # Inefficient checks for violations
        violation = False
        for i in range(len(vals)):
            for j in range(i+1, len(vals)):
                v1, v2 = vals[i], vals[j]

                if v2 in beforeList.keys() and v1 in beforeList[v2]: 
                    violation = True
                    break
                
            # End of inner for loop
            if violation: break

        # End of outer for loop

        # Adding middle page if needed
        if not violation: midNums += vals[int(len(vals) / 2)]

    # End of iterating through lines
    return midNums

def part2():
    data = readFile('inputs/day5.txt')

    # Splitting data into rules and jobs
    rules = []
    jobs = []
    beforeLine = True
    for line in data:
        if line == "": beforeLine = False
        elif beforeLine: rules.append(line)
        else: jobs.append(line)

    # Getting list of dependencies
    beforeList = {} # Keys are jobs, values are jobs they have to be before
    for r in rules:
        vals = r.split('|')
        if int(vals[0]) in beforeList.keys(): beforeList[int(vals[0])].append(int(vals[1]))
        else: beforeList[int(vals[0])] = [int(vals[1])]

    # Iterating through lists of jobs
    midNums = 0
    for l in jobs:
        # Processing input
        vals = l.split(',')
        for i in range(len(vals)): vals[i] = int(vals[i])

        # Inefficient checks for violations
        violation = False
        for i in range(len(vals)):
            for j in range(i+1, len(vals)):
                v1, v2 = vals[i], vals[j]

                if v2 in beforeList.keys() and v1 in beforeList[v2]: 
                    violation = True
                    break
                
            # End of inner for loop
            if violation: break

        # End of outer for loop

        # Skipping already valid input
        if not violation: continue 

        # Identifying violating location(s) and moving as needed
        change = True
        while change:
            change = False
            for i in range(len(vals)):
                for j in range(i+1, len(vals)):
                    v1, v2 = vals[i], vals[j]
                    if v2 in beforeList.keys() and v1 in beforeList[v2]: 

                        # Moving v2 directly before v1
                        temp = v2
                        for k in range(j, i, -1): vals[k] = vals[k-1]
                        vals[i] = temp
                        change = True
                        break
                
                # End of inner for loop
                if change: break
            # End of outer for loop
        
        # Adding middle page
        midNums += vals[int(len(vals) / 2)]

    # End of iterating through lines
    return midNums

answer1 = part1()
answer2 = part2()
print(answer1, answer2)