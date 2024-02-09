# Problem F
s = input()
count = 0
yCount = 0

for ch in s:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u': count += 1
    if ch == 'y': yCount += 1
        
print(count, count+yCount)
