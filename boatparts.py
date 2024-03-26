""" Boat Parts """
vals = input().split()
p = int(vals[0])
n = int(vals[1])

output = "paradox avoided"
parts = set()
for i in range(n):
    thisPart = input()
    parts.add(thisPart)
    if output == "paradox avoided" and len(parts) == p:
        output = str(i+1)
print(output)