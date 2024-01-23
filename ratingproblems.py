# Problem A
vals = input().split()
n = int(vals[0])
k = int(vals[1])

sum = 0
for i in range(k):
    sum += int(input())
    
str = f"{(sum + -3.0 * (n - k)) / n} {(sum + 3.0 * (n - k)) / n}"
print(str)