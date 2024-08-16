# ballotboxes.py
# HEAP PROBLEM
""" NOT EFFICIENT ENOUGH. NEXT STEP WOULD BE TO TRY CPP"""

import heapq

line = input()
while line != "-1 -1":
    vals = line.split()
    n = int(vals[0])
    b = int(vals[1])
    b -= n # Because each city needs at least one ballot box

    # Creating inital min heap
    pops = []
    for i in range(n):
        heapq.heappush(pops,  (-1 * int(input()), 1) ) # Using opposite of each population
    blankline = input()

    # Assigning each heap to city with most voters per box
    for i in range(b):
        thisTuple = heapq.heappop(pops)
        newTuple = (thisTuple[0] * thisTuple[1] / (thisTuple[1] + 1), thisTuple[1] + 1)
        heapq.heappush(pops, newTuple)

    # Getting maximum number of people per ballot box
    maxTuple = heapq.heappop(pops)
    cityPop = -1 * maxTuple[0] * maxTuple[1]
    avePop = int(cityPop / maxTuple[1])
    if cityPop % maxTuple[1] != 0: avePop += 1

    print(avePop)

    line = input()

    
