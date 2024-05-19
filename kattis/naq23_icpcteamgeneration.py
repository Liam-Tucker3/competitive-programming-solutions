# Problem E
n = int(input())
ranks = []
for i in range(1, n+1):
    vals = input().split()
    ranks.append((i, int(vals[0]), int(vals[1])))

count = 0
i = 0

while i < n:
    if i+2 >= n: break
    
    if ranks[i][0] >= ranks[i+2][1] and ranks[i+2][0] <= ranks[i][2]:
        count += 1
        i += 3
        continue
    i+= 1

print(count)
