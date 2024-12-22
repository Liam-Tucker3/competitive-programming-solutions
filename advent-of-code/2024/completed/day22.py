# Importing useful function
from utils import readFile, toGrid, printGrid

def part1():
    def calcSecretNum(num, g):
        for i in range(g):
            newNum = 64 * num
            num = (newNum ^ num) % 16777216
            newNum = int(num / 32)
            num = (newNum ^ num) % 16777216
            newNum = 2048 * num
            num = (newNum ^ num) % 16777216
        return num


    data = readFile('inputs/day22.txt')

    keySum = 0
    for num in data:
        num = int(num)
        key = calcSecretNum(num, 2000)
        # print(key)
        keySum += key
    return keySum
        

def part2():
    def calcSecretNum(num, g):
        prices = [num % 10]
        for i in range(g):
            newNum = 64 * num
            num = (newNum ^ num) % 16777216
            newNum = int(num / 32)
            num = (newNum ^ num) % 16777216
            newNum = 2048 * num
            num = (newNum ^ num) % 16777216
            prices.append(num % 10)
        return prices
    
    def toDict(prices):
        d = {}
        for i in range(4, len(prices)):
            s = f"{prices[i-3] - prices[i-4]}_{prices[i-2] - prices[i-3]}_{prices[i-1] - prices[i-2]}_{prices[i] - prices[i-1]}"
            if s not in d: d[s] = prices[i]
        return d


    data = readFile('inputs/day22.txt')

    # Getting dict of counts
    allDict = {}
    for num in data:
        num = int(num)
        prices = calcSecretNum(num, 2000)
        thisDict = toDict(prices)
        for k in thisDict.keys():
            if k in allDict: allDict[k] += thisDict[k]
            else: allDict[k] = thisDict[k]
    
    # Getting max
    maxVal = -1
    for k in allDict.keys(): maxVal = max(maxVal, allDict[k]) 

    return maxVal
    

answer1 = part1()
answer2 = part2()
print(answer1, answer2)