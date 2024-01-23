inpStr = str(input())
passStr = inpStr.split(" ")[0]
realStr = inpStr.split(" ")[1]

counter_i = 0
compStr = ""
m = dict()

for c in passStr:
    if (c in m):
        m[c]+=1
    else:
        m[c] = 1

for c in realStr:
    if ((c in passStr) and (c in m) and (m[c] > 0)):
        compStr += c
        counter_i+=1
        m[c]-=1

    if (compStr != passStr[0:counter_i]):
        print("FAIL")
        quit()
    
if (compStr == passStr):
    print("PASS")
else:
    print("FAIL")
