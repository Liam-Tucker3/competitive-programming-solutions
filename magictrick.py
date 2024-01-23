# Problem B
str = input()
dict = {}
result = 1
for ch in str:
    if ch in dict.keys(): 
        result = 0
        break
    dict[ch] = 1
print(result)