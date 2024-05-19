import math
n=int(input())
l=[]
for i in range(n):
    x=input().split()
    for i in range(3):
        x[i]=int(x[i])
    l.append(x)
q=[]
s=0
for j in range(n):
    s=l[j][0]+(l[j][1]*l[j][2])/math.gcd(l[j][1],l[j][2])
    q.append(s)
print(int(min(q)))
