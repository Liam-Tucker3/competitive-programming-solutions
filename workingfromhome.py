# Working From Home
import math
vals = input().split()
m = int(vals[0])
p = int(vals[1])
n = int(vals[2])
adj = 0

times = []
for i in range(n):
    times.append(int(input()))

episodeCount = 0
adj = 0
for t in times:
    # print("Goal/adj/workTime", m, adj, t)
    if math.ceil(m - adj) <= t: episodeCount += 1
    adj = p * (t - math.ceil(m - adj)) / 100

print(episodeCount)
