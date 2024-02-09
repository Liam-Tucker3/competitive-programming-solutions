# Problem F: Tractor
n = int(input())
for i in range(n):
    vals = input().split()
    a = int(vals[0])
    b = int(vals[1])
    
    big = max(a, b)
    small = min(a, b)
    
    count = 1
    n = 1
    while (2 ** n) - 1 <= big+small:
        if (2 **n)-1 <= small: count += 2**(n) # 
        elif (2 **n)-1 <= big: count += (1 + small)
        else: count += (big + small + 2 - (2 **n))
        n += 1
        
    print(count)
