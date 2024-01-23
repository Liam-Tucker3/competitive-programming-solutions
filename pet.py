#  Problem A
vals = []
for i in range(5):
    vals.append(input().split())

scores = []
for i in range(len(vals)):
    x = 0
    for j in range(len(vals[i])):
         x += int(vals[i][j])
    scores.append(x)
        
max_index = 1
max_score = 0
for i in range(5):
    if scores[i] > max_score:
        max_score = scores[i]
        max_index = i+1
        
print(max_index, max_score)