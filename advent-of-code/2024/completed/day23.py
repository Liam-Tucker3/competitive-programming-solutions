# Importing useful function
from utils import readFile, toGrid, printGrid
from itertools import combinations

def part1():
    data = readFile('inputs/day23.txt')

    # Getting connection dictionary
    conn = {}
    for line in data:
        vals = line.split('-')
        v1, v2 = vals[0], vals[1]
        if v1 in conn.keys(): conn[v1].append(v2)
        else: conn[v1] = [v2]
        if v2 in conn.keys(): conn[v2].append(v1)
        else: conn[v2] = [v1]

    triples = set()

    # Finding all triples
    for ch in "abcdefghijklmnopqrstuvwxyz":
        c = f"t{ch}"
        if c not in conn.keys(): continue

        vals = conn[c]
        for i in range(len(vals)):
            for j in range(i):
                v1, v2 = vals[i], vals[j]
                if v1 in conn[v2]:
                    theseVals = sorted([v1, v2, c])
                    triples.add(f"{theseVals[0]}_{theseVals[1]}_{theseVals[2]}")

    print(len(conn.keys()))
    maxConns = 0
    for k in conn.keys():
        maxConns = max(maxConns, len(conn[k]))
    print(maxConns)
    return len(triples)

def part2():
    def findNples(conn, n):
        ops = set()
        # for ch in "abcdefghijklmnopqrstuvwxyz":
        #     c = f"t{ch}"
        #     if c not in conn.keys(): continue
        for c in conn.keys():

            vals = conn[c]
            combos = list(combinations(vals, n-1))
            for combo in combos:
                if len(combo) < n-1: continue
                works = True
                for i in range(len(combo)):
                    for j in range(i):
                        if combo[i] not in conn[combo[j]]: 
                            works = False
                            break
                    if not works: break
                if works:
                    newCombo = [c]
                    for thisVal in combo: newCombo.append(thisVal)
                    # combo.append(c)
                    newCombo = list(sorted(newCombo))
                    ops.add(",".join(newCombo))

        return ops

    data = readFile('inputs/day23.txt')

    # Getting connection dictionary
    conn = {}
    for line in data:
        vals = line.split('-')
        v1, v2 = vals[0], vals[1]
        if v1 in conn.keys(): conn[v1].append(v2)
        else: conn[v1] = [v2]
        if v2 in conn.keys(): conn[v2].append(v1)
        else: conn[v2] = [v1]

    for i in range(2, 14):
        ops = findNples(conn, i)
        print(i, len(ops))
        if len(ops) == 1: return list(ops)[0]
        if len(ops) == 0: return 0
        
    return 0


answer1 = part1()
answer2 = part2()
print(answer1, answer2)