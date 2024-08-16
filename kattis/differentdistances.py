# differentdistances.py

vals = input()

while vals != "0":
    vals = vals.split()

    x1 = float(vals[0])
    y1 = float(vals[1])
    x2 = float(vals[2])
    y2 = float(vals[3])
    p = float(vals[4])

    xdiff = x2 - x1
    if xdiff < 0: xdiff *= -1
    ydiff = y2 - y1
    if ydiff < 0: ydiff *= -1

    val = (xdiff ** p + ydiff ** p) ** (1/p)
    print(val)

    vals = input()