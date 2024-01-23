#H
n=int(input())
s=input()
n=len(s)
a="Adrian"
b="Bruno"
c="Goran"
la=['A','B','C']*n
lb=['B','A','B','C']*n
lc=['C','C','A','A','B','B']*n
ca=0
cb=0
cc=0
for i in range(len(s)):
    if s[i]==la[i]:
        ca=ca+1
    if s[i]==lb[i]:
        cb=cb+1
    if s[i]==lc[i]:
        cc=cc+1
l=[ca,cb,cc]
m=max(l)
print(m)
if m==ca:
    print(a)
if m==cb:
    print(b)
if m==cc:
    print(c)