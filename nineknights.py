def update_coverage(covered, i, j):
    if i-2 >= 0 and j-1 >= 0: covered[i-2][j-1] = 1
    if i-2 >= 0 and j+1 <= 4: covered[i-2][j+1] = 1
    if i+2 <= 4 and j+1 <= 4: covered[i+2][j+1] = 1
    if i+2 <= 4 and j-1 >= 0: covered[i+2][j-1] = 1
        
    if i-1 >= 0 and j-2 >= 0: covered[i-1][j-2] = 1
    if i-1 >= 0 and j+2 <= 4: covered[i-1][j+2] = 1
    if i+1 <= 4 and j+2 <= 4: covered[i+1][j+2] = 1
    if i+1 <= 4 and j-2 >= 0: covered[i+1][j-2] = 1
        
    return covered
    
# Problem C
arr = []
indexes = []
for i in range(5):
    arr += input().split()
    
covered = [[0 for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(5):
        if arr[i][j] == "k": 
            indexes.append((i, j))
            covered = update_coverage(covered, i, j)
        
str = "valid"
if len(indexes) != 9: str = "invalid"
for t in indexes:
    if covered[t[0]][t[1]] == 1: 
        str = "invalid"
        break

print(str)
    