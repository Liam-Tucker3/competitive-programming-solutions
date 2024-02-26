#### H: Abridged Reading
vals = input().split()
n = int(vals[0])
m = int(vals[1])

pages = [0 for i in range(n)]
i = 0
while (i < n):
    vals = input().split()
    for j in range(len(vals)):
        pages[i] = int(vals[j])
        i += 1
    
dependencies = {}
culminatingChapters = set()
for i in range(len(pages)):
    dependencies[i+1] = []
    culminatingChapters.add(i+1)
    
for i in range(m):
    vals = input().split()
    a = int(vals[0])
    b = int(vals[1])
    
    dependencies[b].append(a)
    if a in culminatingChapters: culminatingChapters.remove(a)
    
noUpdate = False
while True:
    if noUpdate: break
        
    noUpdate = True    
    toCheck = list(dependencies.keys())
    for k in toCheck: # Iterating though every key in dependencies
        if len(dependencies[k]) == 0: continue # This chapter has no dependencies -> no need ton keep iterating
            
        for d in dependencies[k]: # Iterating through every chapter the current chapter is dependent on
            for j in dependencies[d]: # Iterating through every chapter that chapter depends on
                if j not in dependencies[k]: 
                    dependencies[k].append(j)
                    noUpdate = False
            
assert len(culminatingChapters) >= 2
culminatingChapters = list(culminatingChapters)
minScore = 9999999

for i in range(len(culminatingChapters)):
    for j in range(len(culminatingChapters)):
        if i == j: continue
        
        allChapters = set()
        allChapters.add(culminatingChapters[i])
        allChapters.add(culminatingChapters[j])
        
        for d in dependencies[culminatingChapters[i]]: allChapters.add(d)
        for d in dependencies[culminatingChapters[j]]: allChapters.add(d)
            
        allChapters = list(allChapters)
        score = 0
        for a in allChapters:
            if a > len(pages) or a <= 0:
                print("FAILURE")
                continue
            score += pages[a-1]
        minScore = min(score, minScore)
        
print(minScore)
