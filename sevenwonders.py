# Problem A
str = input()

t = 0
c = 0
g = 0

for ch in str:
    if ch == "T": t += 1
    if ch == "C": c += 1
    if ch == "G": g += 1
        
result = 7 * min(g, t, c) + g*g + c*c + t*t
print(result)