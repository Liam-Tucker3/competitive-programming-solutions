# distance.py

n = int(input())

streets = [0 for i in range(n)]
avenues = [0 for i in range(n)]

for i in range(n):
    vals = input().split()
    streets[i] = int(vals[0])
    avenues[i] = int(vals[1])

sumDistance = 0

streets = sorted(streets)
avenues = sorted(avenues)

for i in range(n):
    sumDistance += streets[i] * (n-1 - 2 * (n-1-i))
    sumDistance += avenues[i] * (n-1 - 2 * (n-1-i))

print(sumDistance)