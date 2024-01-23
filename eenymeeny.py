num = len(input().split())
n = int(input())
i = 0

teamA = []
teamB = []
index = -1
names = []
for j in range(n): names.append(input())
    
while len(names) > 0:
    index = (index + num) % len(names)
    thisName = names[index]
    if i % 2 == 0: teamA.append(thisName)
    else: teamB.append(thisName)
    i += 1
    
    names = names[:index] + names[index+1:]
    index -= 1
    
print(len(teamA))
for n in teamA: print(n)
print(len(teamB))
for n in teamB: print(n)