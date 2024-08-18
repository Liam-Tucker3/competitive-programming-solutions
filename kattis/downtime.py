# downtime.py
# Two Pointer

vals = input().split()
n = int(vals[0])
k = int(vals[1])

timestamps = []
for i in range(n):
    timestamps.append(int(input()))

l = 0
r = 0

maxSimultaneous = 1 # n guaranteed to be >= 1

while r+1 < n:
    r += 1
    while timestamps[l] + 1000 <= timestamps[r] and l < r: l += 1
    maxSimultaneous = max(maxSimultaneous, r-l)

# Edge case: the everything is simultaneous
if timestamps[0] + 1000 > timestamps[-1]: maxSimultaneous = len(timestamps)

serversNeeded = int(maxSimultaneous / k)
if maxSimultaneous % k != 0: serversNeeded += 1
print(serversNeeded)