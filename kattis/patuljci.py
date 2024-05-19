# Problem G
vals = []
for i in range(9):
    vals.append(int(input()))
    
done = False
final_vals = []
for i in range(9):
    if done: break
    for j in range(9):
        if done: break
        if i == j: continue
        
        temp = []
        for k in range(9):
            if k != i and k != j: temp.append(vals[k])
        x = sum(temp)
        if x == 100:
            for val in temp:
                if not done: final_vals.append(val)
            done = True
            
for f in final_vals: print(f)