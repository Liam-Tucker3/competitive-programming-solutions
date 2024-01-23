#b
n=list(input().split(" "))
if n[0]=='E':
    s=n[1]
    c=0
    count=1
    i=0
    br=0
    while i<len(s):
        while i+1 < len(s) and s[i]==s[i+1]:
            count=count+1
            i=i+1
        print(s[i],count,sep="",end="")
        count=1
        i=i+1
        
                





else:
    i=0
    s=n[1]   
    while i <len(s):
        print(s[i]*int(s[i+1]),end="")
        i=i+2
     
