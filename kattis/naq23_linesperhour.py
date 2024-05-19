# Problem G
vals = input().split()
n = int(vals[0])
lph = 5 * int(vals[1])

problems = []
for i in range(n):
    problems.append(int(input()))

problems = sorted(problems)
# print(problems)
# print(lph)

count = 0
while True:
    if len(problems) > count and problems[count] <= lph:
        lph -= problems[count]
        count += 1
        # print(count, lph)
    else:
        break
        
print(count)
