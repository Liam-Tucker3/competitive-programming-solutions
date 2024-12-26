# Importing useful function
from utils import readFile, toGrid, printGrid

def part1():
    # Hardcoding inputs
    a, b, c = 47792830, 0, 0
    data = "2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0".split(",")
    for i in range(len(data)): data[i] = int(data[i])

    # Performing operations
    outputs = []
    ip = 0
    while ip < len(data) - 1:
        x, y = data[ip], data[ip+1]
        # print(ip, x, y)
        # Getting combo operand
        if y <= 3: combo = y
        if y == 4: combo = a
        if y == 5: combo = b
        if y == 6: combo = c
        if y == 7: combo = "ERROR" # Should never run


        if x == 0: a = int(a / 2**combo)
        elif x == 1: b = b ^ y
        elif x == 2: b = combo % 8
        elif x == 3:
            if a != 0: 
                ip = y
                continue
        elif x == 4: b = b ^ c
        elif x == 5: outputs.append(combo % 8)
        elif x == 6: b = int(a / 2**combo)
        elif x == 7: c = int(a / 2**combo)
        else: print("ERROR")

        ip += 2
    # End of while
    for i in range(len(outputs)): outputs[i] = str(outputs[i])
    return ",".join(outputs)

# Borrowing ideas from https://github.com/ading2210/advent-of-code-solutions/blob/main/2024/day17/day17.py
def part2():
    def octal(l):
        c = 0
        for i in range(len(l)): c += (8**(15-i)) * l[i]
        return c

    def prog(a, b, c, data):
        for i in range(len(data)): data[i] = int(data[i])

        # Performing operations
        outputs = []
        ip = 0
        while ip < len(data) - 1:
            x, y = data[ip], data[ip+1]
            # print(ip, x, y)
            # Getting combo operand
            if y <= 3: combo = y
            if y == 4: combo = a
            if y == 5: combo = b
            if y == 6: combo = c
            if y == 7: combo = "ERROR" # Should never run


            if x == 0: a = int(a / 2**combo)
            elif x == 1: b = b ^ y
            elif x == 2: b = combo % 8
            elif x == 3:
                if a != 0: 
                    ip = y
                    continue
            elif x == 4: b = b ^ c
            elif x == 5: outputs.append(combo % 8)
            elif x == 6: b = int(a / 2**combo)
            elif x == 7: c = int(a / 2**combo)
            else: print("ERROR")

            ip += 2
        # End of while
        for i in range(len(outputs)): outputs[i] = str(outputs[i])
        return ",".join(outputs)
    # End of program

    # 
    def findVal(target, data):
        output = []
        matched = target[-1:] #the last n digits of the program
        initA = 8 ** 15 #this is the minimum value required to have a 16 digit output
        power = 14 #increment by 8 ** 13 to begin with

        while output != matched:
            initA += 8 ** power
            output = prog(initA, 0, 0, data)
            #when the digits match, decrement the power by 1
            #by decreasing the power, the matched digits will no longer change
            if output[-len(matched):] == matched:
                power = max(0, power - 1)
                matched = target[-(len(matched)+1):]

        return initA


    data = "2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0".split(",")
    for i in range(len(data)): data[i] = int(data[i])

    val = findVal(data, data)
    return val
    

answer1 = part1()
answer2 = part2()
print(answer1, answer2)