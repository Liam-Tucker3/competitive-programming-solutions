n=int(input())
l=list(input().split(' '))
for i in range(len(l)):
    l[i]=int(l[i])
i=0
c=1
while i< len(l)-1:
    if l[i] < l[i+1]:
        c=c+1
    i=i+1
print(c)
   