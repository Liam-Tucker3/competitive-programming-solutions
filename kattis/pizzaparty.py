n = int(input())

strs = [input() for i in range(n)]
for i in range(len(strs)):
    s = strs[i]
    words = s.split(' ')
    if len(words) == 1: 
        strs[i] = [s]
    else:
        newList = []
        newList.append(words[-1])
        conditions = []
        for j in range(int(len(words) / 2 - 1)):
            conditions.append(words[2*j+1])
        newList.append(conditions)
        newList.append(words[2])
        strs[i] = newList


toppings = set()

change = True

# print(strs)

while change:
    change = False
    newStrs = []

    for s in strs:
        if len(s) == 1: # No conditional
            toppings.add(s[0])
        else:
            if s[0] in toppings: continue # Already in pizza so we can ignore this
            top = s[0]
            conditions = s[1]
            conditional = s[2]
            
            # Case 1: Only one condition
            if len(conditions) == 1:
                if conditions[0] in toppings: 
                    toppings.add(top)
                    continue
                else:
                    newStrs.append(s)
                    continue

            # Case 2: Multiple conditions, and
            if conditional == "and":
                toAdd = True
                for c in conditions:
                    if c not in toppings:
                        newStrs.append(s)
                        toAdd = False
                        break
                if toAdd: toppings.add(top)
                continue
        
            # Case 3: Multiple conditions, or
            for c in conditions:
                toSkip = False
                if c in toppings:

                    toppings.add(top)
                    toSkip = True
                    break
            if toSkip: newStrs.append(s)
            continue

    # print(strs, newStrs)
    if len(newStrs) != len(strs): change = True
    strs = newStrs

print(len(toppings))

"""
4
peppers
if spinach and olives then tomatoes
spinach
feta

4
pepperoni
sausage
if pepperoni and sausage then mushrooms
if mushrooms or peppers then cheese

"""