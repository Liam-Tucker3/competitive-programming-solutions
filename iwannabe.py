""" I Wanna Be The Very Best"""
vals = input().split()
n = int(vals[0])
k = int(vals[1])

attacks = []
defends = []
healths = []

for i in range(n):
    vals = input().split()
    a = int(vals[0])
    d = int(vals[1])
    h = int(vals[2])
    
    attacks.append( (a, str(a), str(d), str(h)) )
    defends.append( (d, str(a), str(d), str(h)) )
    healths.append( (h, str(a), str(d), str(h)) )
    
attacks = list(reversed(sorted(attacks)))
defends = list(reversed(sorted(defends)))
healths = list(reversed(sorted(healths)))

bestList = set()
for i in range(k):
    pA = attacks[i]
    pD = defends[i]
    pH = healths[i]
    
    bestList.add(''.join([pA[1], pA[2], pA[3]]))
    bestList.add(''.join([pD[1], pD[2], pD[3]]))
    bestList.add(''.join([pH[1], pH[2], pH[3]]))
    
print(len(bestList))