# Problem L
vals = input().split()
n = int(vals[0])
a = int(vals[1])
b = int(vals[2])

hadMin = False
hadMax = False
possible = True

for i in range(n-1):
    val = int(input())
    if val < a or val > b:
        possible = False
        continue
    elif a == val: hadMin = True
    elif b == val: hadMax = True
        
if not possible or (not hadMin and not hadMax):
    print(-1)
else:
    if not hadMin: print(a)
    elif not hadMax: print(b)
    else:
        for i in range(a, b+1):
            print(i)
