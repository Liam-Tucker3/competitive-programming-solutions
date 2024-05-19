# Problem D
vals = input().split()
h = int(vals[0])

if len(vals) == 1:
    print(2 ** (h+1) - 1)
else:
    s = vals[1]

    levelSize = 2 ** (len(s))
    offset = (2 ** (h+1)) - (2 ** (len(s) + 1))

    score = 1 + offset
    for i in range(len(s)):
        if s[i] == "L": score += (2 ** (len(s) - 1 -i))

    print(score)