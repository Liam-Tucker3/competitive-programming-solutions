n = int(input())

lastChar = -1
for i in range(n):
    val = int(input())
    if lastChar == -1:
        lastChar = val
        continue

    if val % lastChar == 0:
        print(val)
        lastChar = -1
    