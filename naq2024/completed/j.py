# Menger Sponge
import math

vals = input().split()
l = int(vals[0])
xN = int(vals[1])
xD = int(vals[2])
yN = int(vals[3])
yD = int(vals[4])
zN = int(vals[5])
zD = int(vals[6])


output = 1

for i in range(l):
    xF = 1.0 * xN / xD
    yF = 1.0 * yN / yD
    zF = 1.0 * zN / zD

    # print(xF, yF, zF)
    
    # Checking for out of cube on this level
    if xF > 1.0/3.0 and xF < 2.0/3.0 and yF > 1.0/3.0 and yF < 2.0/3.0 and zF > 1.0/3.0 and zF < 2.0/3.0: # Case 1
        output = 0
        break
    if xF > 1.0/3.0 and xF < 2.0/3.0 and yF > 1.0/3.0 and yF < 2.0/3.0 and zF > 2.0/3.0: # Case 2
        output = 0
        break
    if xF > 1.0/3.0 and xF < 2.0/3.0 and yF > 1.0/3.0 and yF < 2.0/3.0 and zF < 1.0/3.0: # Case 3
        output = 0
        break
    if xF > 1.0/3.0 and xF < 2.0/3.0 and zF > 1.0/3.0 and zF < 2.0/3.0 and yF > 2.0/3.0: # Case 2
        output = 0
        break
    if xF > 1.0/3.0 and xF < 2.0/3.0 and zF > 1.0/3.0 and zF < 2.0/3.0 and yF < 1.0/3.0: # Case 3
        output = 0
        break
    if zF > 1.0/3.0 and zF < 2.0/3.0 and yF > 1.0/3.0 and yF < 2.0/3.0 and xF > 2.0/3.0: # Case 2
        output = 0
        break
    if zF > 1.0/3.0 and zF < 2.0/3.0 and yF > 1.0/3.0 and yF < 2.0/3.0 and xF < 1.0/3.0: # Case 3
        output = 0
        break

    # Updating coordinates
    if 3 * xN <= xD: 
        xN *= 3
    elif 3 * xN <= 2 * xD: 
        xN = 3 * xN - xD
        # xD *= 3
    else: 
        xN = 3*xN - 2 * xD
        # xD *= 3

    if 3*yN <= yD: 
        yN *= 3
    elif 3*yN <= 2*yD: 
        yN = 3 * yN - yD
        # yD *= 3
    else: 
        yN = 3*yN - 2 * yD
        # yD *= 3
        
    if 3*zN <= zD: 
        zN *= 3
    elif 3*zN <= 2*zD: 
        zN = 3 * zN - zD
        # zD *= 3
    else: 
        zN = 3*zN - 2 * zD
        # zD *= 3

    xGCD = math.gcd(xN, xD)
    xN = int(xN / xGCD)
    xD = int(xD / xGCD)

    yGCD = math.gcd(yN, yD)
    yN = int(yN / yGCD)
    yD = int(yD / yGCD)

    zGCD = math.gcd(zN, zD)
    zN = int(zN / zGCD)
    zD = int(zD / zGCD)

print(output)

