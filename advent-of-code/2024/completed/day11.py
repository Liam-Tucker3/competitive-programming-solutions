# Importing useful function
from utils import readFile

def part1():
    def nextGen(num, completedGenerations):
        if completedGenerations == 25: return 1
        if num == 0: return nextGen(1, completedGenerations+1)
        if len(str(num)) % 2 == 0: 
            s = str(num)
            l = len(str(num))
            v1 = nextGen(int(s[:int(l/2)]), completedGenerations+1)
            v2 = nextGen(int(s[int(l/2):]), completedGenerations+1)
            return v1 + v2
        else: return nextGen(num*2024, completedGenerations+1)


    data = readFile('inputs/day11.txt')[0]
    vals = data.split(' ')
    count = 0
    for i in range(len(vals)):
        count += nextGen(int(vals[i]), 0)
    return count

def part2():
    def sim(l):
        d = {}
        for val in l:
            if val in d.keys(): d[val] += 1
            else: d[val] = 1
        
        # Simulating
        for i in range(75):
            newD = {}
            # Iterating through vals to check
            for val in list(d.keys()):
                # Finding the new values(s) of the stone
                if val == 0: newVal = [1]
                elif len(str(val)) % 2 == 0:
                    s = str(val)
                    sLen = len(str(val))
                    v1 = int(s[:int(sLen/2)])
                    v2 = int(s[int(sLen/2):])
                    newVal = [v1, v2]
                else:
                    newVal = [2024*val]
                # Adding to new dictionary
                for v in newVal:
                    if v in newD.keys(): newD[v] += d[val]
                    else: newD[v] = d[val]

            # Updating static vals
            d = newD
            if i == 74:
                count = 0
                for v in d.keys(): count += d[v]
                return count
        # End of iterations

    # End of sim function
    


    data = readFile('inputs/day11.txt')[0]
    vals = data.split(' ')
    for i in range(len(vals)): vals[i] = int(vals[i])
    print(vals)
    return sim(vals)

answer1 = part1()
answer2 = part2()
print(answer1, answer2)