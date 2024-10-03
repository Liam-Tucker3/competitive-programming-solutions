str = input()
count = 0
for ch in str:
    if ch == "|": count += 1
    else: break

if len(str) == 2 * count + 2: print("correct")
else: print("fix")