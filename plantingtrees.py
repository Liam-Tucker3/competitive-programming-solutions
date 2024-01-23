# Problem C
n = int(input())
days = input().split()
for i in range(len(days)):
    days[i] = -1 * int(days[i])
days = sorted(days)
for i in range(len(days)):
    days[i] = -1 * days[i] + 2 + i
    
print(max(days))