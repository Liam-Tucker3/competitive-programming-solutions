# Problem C
vals = input().split()
n = int(vals[0])
m = int(vals[1])
k = int(vals[2])

time_before = 0
for i in range(n):
    thisLine = input().split()
    title = ""
    if len(thisLine) == 2: title = thisLine[0][1:-1]
    else: 
        for j in range(0, len(thisLine) - 1):
            if j == 0: title += thisLine[j][1:]
            elif j == len(thisLine) - 2: title += " " + thisLine[j][:-1]
            else: title += " " + thisLine[j]
        
    # print(title)
    if title < "Jane Eyre":
        time_before += int(thisLine[-1])

books = []
for i in range(m):
    thisLine = input().split()
    # print(thisLine)
    title = ""
    if len(thisLine) == 3: title = thisLine[1][1:-1]
    else: 
        for j in range(1, len(thisLine) - 1):
            if j == 1: title += thisLine[j][1:]
            elif j == len(thisLine) - 2: title += " " + thisLine[j][:-1]
            else: title += " " + thisLine[j]
        
    if title < "Jane Eyre":
        if int(thisLine[0]) <= time_before:
            time_before += int(thisLine[-1])
        else:
            t = (int(thisLine[0]), int(thisLine[-1]))
            # print(t)
            books.append(t)
            
books = sorted(books)

i = 0
while True:
    if i < len(books) and books[i][0] <= time_before:
        time_before += books[i][1]
        i += 1
    else:
        break

print(time_before + k)