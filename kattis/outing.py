# Problem F

def recurse(grid, currScore, goal, freeTree, graphs, bonuses):
    # print("CScore", currScore, "Goal", goal)
    # print(goal)
    # print(len(graphs), len(bonuses))
    if currScore <= goal and currScore + freeTree >= goal:
        print(goal)
        quit()
        grid[currScore][freeTree] = goal
        return goal
    elif len(graphs) == 0:
        grid[currScore][freeTree] = min(goal, freeTree + currScore)
        return min(goal, freeTree + currScore)
    
    else:
        theseScores = [currScore + freeTree]
        for i in range(len(graphs)):
            if currScore + graphs[i] <= goal:
                grid[currScore + graphs[i]][freeTree + bonuses[i]] =  recurse(grid, currScore + graphs[i], goal, freeTree + bonuses[i], graphs[:i] + graphs[i+1:], bonuses[:i] + bonuses[i+1:])
                theseScores.append(grid[currScore + graphs[i]][freeTree + bonuses[i]])
        grid[currScore][freeTree] = min(goal, max(theseScores))
        return grid[currScore][freeTree] 


vals = input().split()
n = int(vals[0])
kVal = int(vals[1])

require = {}
required = {}
for i in range(n):
    required[i+1] = []
    
people = input().split()
for i in range(len(people)):
    require[i+1] = int(people[i])
    required[int(people[i])].append(i+1)

#print(require)
#print(required)
    
trees = []
ltc = []
items = [i+1 for i in range(n)]
handled = []
for i in range(1, n+1):
    if require[i] == i:
        ltc.append(i)
        
while len(ltc) > 0:
    v = ltc[0]
    # print("V", v)
    ltc= ltc[1:]
    
    trees.append(v)
    handled.append(v)
    items.remove(v)
    newadd = required[v]
    #print(newadd)
    #print(required[v])
    for n in newadd: 
        if n not in handled: ltc.append(n)

# print(trees)
    
loopLists = []

# print(items)
while len(items) > 0:
    # print("ITEMS", items)

    p = items[0]
    
    pNext = require[p]
    if pNext in handled:
        for q in range(len(loopLists)):
            k= loopLists[q]
            if pNext in k[0]:
                loopLists[q][2] += 1
                loopLists[q][0].append(pNext)
                break
        items.remove(p)
        handled.append(p)
        # del require[p]
        # del required[p]
        continue
        
    else:
        thisLoop = [p, pNext]
        # del require[p]
        # del required[p]
        if p in items: items.remove(p)
        handled.append(p)
        p = pNext
        while require[p] not in thisLoop:
            pNext = require[p]
            thisLoop.append(pNext)
            # del required[p]
            if p in items: items.remove(p)
            handled.append(p)
            p = pNext
            
        if p in items: items.remove(p)
        handled.append(p)
        thisFinalList = [p]
        while require[p] not in thisFinalList:
            p = require[p]
            thisFinalList.append(p)
        diff = len(thisFinalList) - len(thisLoop)
        # print("APPENDING")
        loopLists.append([list(set(thisLoop)), len(thisFinalList), -1 * diff])
        
# print(loopLists) 
# print("K", kVal)
gs = []
bs = []
for l in loopLists:
    gs.append(l[1])
    bs.append(l[2])


grid = [[0 for i in range(1001)] for j in range(1001)]
val = recurse(grid, 0, kVal, len(trees), gs, bs)
# print("ANSER", val)
print(val)
