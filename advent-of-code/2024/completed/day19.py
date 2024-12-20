# Importing useful function
from utils import readFile

def part1():
    """s: string of remaining pattern, towels: towel options"""
    def isValid(s, towels):
        if len(s) == 0: return 1
        for t in towels:
            if len(s) >= len(t) and s[:len(t)] == t:
                if isValid(s[len(t):], towels): return 1
        return 0
    
    def isValidBetter(s, td, maxLen):
        if len(s) == 0: return 1
        for i in range(min(maxLen, len(s)), 0, -1):
            if s[:i] in td.keys():
                if isValidBetter(s[i:], td, maxLen): return 1
        return 0
    
    def isValidBest(s, td):
        valids = [0 for i in range(len(s))]
        valids.append(1) #Accessible at valids[-1]
        for i in range(len(s)):
            if   i-1 >= -1 and s[i] in td and valids[i-1] == 1: valids[i] = 1
            elif i-2 >= -1 and s[i-1:i+1] in td and valids[i-2] == 1: valids[i] = 1
            elif i-3 >= -1 and s[i-2:i+1] in td and valids[i-3] == 1: valids[i] = 1
            elif i-4 >= -1 and s[i-3:i+1] in td and valids[i-4] == 1: valids[i] = 1
            elif i-5 >= -1 and s[i-4:i+1] in td and valids[i-5] == 1: valids[i] = 1
            elif i-6 >= -1 and s[i-5:i+1] in td and valids[i-6] == 1: valids[i] = 1
            elif i-7 >= -1 and s[i-6:i+1] in td and valids[i-7] == 1: valids[i] = 1
            elif i-8 >= -1 and s[i-7:i+1] in td and valids[i-8] == 1: valids[i] = 1

            # if s == "brwrr" and i == 3: print(i-2, s[i-1:i+1], valids[i-2], s[i-1:i+1] in td)
            # if s == "brwrr": print(valids)

        # print(s, valids)
        return valids[-2] # Last real index
    

    data = readFile('inputs/day19.txt')
    towels = data[0].split(', ')

    # Getting maximum towel length
    maxTowelLength = 0
    for t in towels: maxTowelLength = max(maxTowelLength, len(t))
    
    # Creating towel dictionary
    towelDict = {}
    for t in towels:
        towelDict[t] = 1

    count = 0
    for i in range(2, len(data)):
        # print(i)
        s = data[i]
        works = isValidBest(s, towelDict)
        # print(works, s)
        count += works
    
    return count

def part2():
    def isValidBest(s, td):
        valids = [0 for i in range(len(s))]
        valids.append(1) #Accessible at valids[-1]
        for i in range(len(s)):
            if i-1 >= -1 and s[i] in td and       valids[i-1] >= 1: valids[i] += valids[i-1]
            if i-2 >= -1 and s[i-1:i+1] in td and valids[i-2] >= 1: valids[i] += valids[i-2]
            if i-3 >= -1 and s[i-2:i+1] in td and valids[i-3] >= 1: valids[i] += valids[i-3]
            if i-4 >= -1 and s[i-3:i+1] in td and valids[i-4] >= 1: valids[i] += valids[i-4]
            if i-5 >= -1 and s[i-4:i+1] in td and valids[i-5] >= 1: valids[i] += valids[i-5]
            if i-6 >= -1 and s[i-5:i+1] in td and valids[i-6] >= 1: valids[i] += valids[i-6]
            if i-7 >= -1 and s[i-6:i+1] in td and valids[i-7] >= 1: valids[i] += valids[i-7]
            if i-8 >= -1 and s[i-7:i+1] in td and valids[i-8] >= 1: valids[i] += valids[i-8]

            # if s == "brwrr" and i == 3: print(i-2, s[i-1:i+1], valids[i-2], s[i-1:i+1] in td)
            # if s == "brwrr": print(valids)

        # print(s, valids)
        return valids[-2] # Last real index
    

    data = readFile('inputs/day19.txt')
    towels = data[0].split(', ')

    # Getting maximum towel length
    maxTowelLength = 0
    for t in towels: maxTowelLength = max(maxTowelLength, len(t))
    
    # Creating towel dictionary
    towelDict = {}
    for t in towels:
        towelDict[t] = 1

    count = 0
    for i in range(2, len(data)):
        # print(i)
        s = data[i]
        works = isValidBest(s, towelDict)
        # print(works, s)
        count += works
    
    return count

answer1 = part1()
answer2 = part2()
print(answer1, answer2)