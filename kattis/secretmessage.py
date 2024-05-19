n=int(input())
for i in range(n):
    x=input()
    sq=1
    k=1
    while len(x)>(k**2):
        k=k+1
    #print(k)
    #print(x)
    # m=[['*']*k]*k
    m = [["*" for i in range(k)] for j in range(k)]
    
    #print(m)
    r=0
    c=0
    p=0
    
    p = 0
    for i in range(k):
        for j in range(k):
            if p < len(x): 
                m[i][j] = x[p]
                p += 1
            
    """
    while p <len(x):
        if c<k:
            m[r][c]=x[p]
            print(x[p])
            c=c+1  
            p=p+1
        else:
            r=r+1
            c=0
    """

    #print(m)
    for i in range(k):
        for j in range(k):
            if m[k-j-1][i]!='*':
                print(m[k-j-1][i],end="")
    print()