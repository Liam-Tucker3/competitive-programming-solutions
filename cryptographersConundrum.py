# Problem C
str = input()
count = 0
for i in range(0, len(str), 3):
    if str[i] != "P": count += 1
    if str[i+1] != "E": count += 1
    if str[i+2] != "R": count += 1
        
print(count)