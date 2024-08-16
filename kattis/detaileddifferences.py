# detaileddifferences.py
n = int(input())
for i in range(n):
    str1 = input()
    str2 = input()
    str3 = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]: str3 += "."
        else: str3 += "*"
    print(str1)
    print(str2)
    print(str3)
    print()