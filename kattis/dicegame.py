gunner = input()
emma = input()

gunner = gunner.split()
emma = emma.split()

gc = 0
ec = 0
for i in range(4):
    gc += int(gunner[i])
    ec += int(emma[i])

if gc > ec: print("Gunnar")
if ec > gc: print("Emma")
if gc == ec: print("Tie")