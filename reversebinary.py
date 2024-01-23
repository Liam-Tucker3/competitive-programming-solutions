# Problem A
val = int(input())
digs = []
i = 30
while i >= 0:
    if val >= 2**i:
        digs.append(1)
        val -= 2**i
    else:
        digs.append(0)
    i -= 1
    
while digs[0] == 0: digs = digs[1:]
    
newval = 0
for i in range(len(digs)):
    newval += digs[i] * (2 ** i)
    
print(newval)