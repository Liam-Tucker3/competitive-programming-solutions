# Call for problems

n = int(input())
c = 0
for i in range(n):
    v = int(input())
    if v % 2 == 1: c += 1
print(c)