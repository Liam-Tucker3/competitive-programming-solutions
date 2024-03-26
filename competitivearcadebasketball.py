""" Competitive Basketball Arcade """
vals = input().split()
n = int(vals[0])
p = int(vals[1])
m = int(vals[2])

scores = {}
for i in range(n):
    name = input()
    scores[name] = 0
    
winners = []
    
for i in range(m):
    vals = input().split()
    thisName = vals[0]
    thisScore = int(vals[1])
    if scores[thisName] >= 0:
        scores[thisName] += thisScore
        if scores[thisName] >= p: 
            winners.append(thisName)
            scores[thisName] = -1
            
if len(winners) == 0:
    print("No winner!")
else:
    for w in winners:
        print(f"{w} wins!")