# Problem G
import math
small_factorials = {}
small_factorials[1] = 1
for i in range(2, 16):
    small_factorials[i] = small_factorials[i-1] * i
    

    
str = input()
l = len(str)
if l <= 13:
    for i in range(1, 16):
        if small_factorials[i] == int(str):
            print(i)
            break

else:
    x = 1
    i = 2
    while True:
        x += math.log(i, 10)
        if int(x) == l:
            print(i)
            break
        i += 1