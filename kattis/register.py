# Problem A

registers = [2, 3, 5, 7, 11, 13, 17, 19]
values = [0 for i in range(len(registers))]
for i in range(len(registers)):
    values[i] = 1
    for j in range(i):
        values[i] *= registers[j]
        
num_left = 2*3*5*7*11*13*17*19 - 1
this_score = 0

inputs = input().split()
for i in range(len(inputs)):
    val = int(inputs[i])
    this_score += val * values[i]
print(num_left - this_score)

