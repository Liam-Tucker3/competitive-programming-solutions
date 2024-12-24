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

def part2():
    def octal(l):
        c = 0
        for i in range(len(l)): c += (8**i) * l[i]
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

    # Hardcoding inputs
    inputData = "2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0"
    sampleInputData = "0,3,5,4,3,0"
    data = inputData.split(",")
    sampleData = sampleInputData.split(",")
    sampleI = 117000
    i = 1122450000
    """
    for j in range(8):
        for i in range(1,11):
            outputs = prog(8**i + j, 0, 0, data)
            print(outputs)
    """
    # print("Start values")
    # for i in range(9): print(prog(i, 0, 0, data))
    # print("END of values")
    print("TARGET: 2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0")

    # Generating from front
    # print(prog(octal([1]), 0, 0, data))
    # print("TEST")
    # for i in range(8): print(prog(octal([i, 1]), 0, 0, data))

    for i in range(8):
        for j in range(8):
            for k in range(8):
                print(i, j, k, prog(8**15 * i + 8**14 + j + 8**13 * k, 0, 0, data))

    # Generating from back
    """
    print(prog(octal([3]), 0, 0, data))
    print(prog(octal([5, 3]), 0, 0, data))
    print(prog(octal([5, 5, 3]), 0, 0, data))
    print(prog(octal([0, 5, 5, 3]), 0, 0, data))
    print(prog(octal([3, 0, 5, 5, 3]), 0, 0, data))
    print(prog(octal([2, 3, 0, 5, 5, 3]), 0, 0, data))
    print(prog(octal([2, 3, 0, 5, 5, 3]), 0, 0, data))
    print(prog(octal([3, 2, 3, 0, 5, 5, 3]), 0, 0, data))
    print(prog(octal([2, 3, 2, 3, 0, 5, 5, 3]), 0, 0, data))
    # print(prog(octal([5, 2, 3, 0, 5, 5, 3]), 0, 0, data))
    for i in range(8): print(prog(octal([i, 2, 3, 2, 3, 0, 5, 5, 3]), 0, 0, data))
    """
    print("This test")
    """
    for i in range(8): 
        for j in range(8):
            print(prog(octal([i, j, 2, 5, 2, 3, 0, 5, 5, 3]), 0, 0, data))
    """

    # for i in range(8): print(i, prog(octal([5, 5, 3, i]), 0, 0, data))
    # print(prog(512*3+64*5+8*5+3, 0, 0, data))


    """
    while True:
        if i % 10000 == 0: print(i)
        outputData = prog(i, 0, 0, data)
        if outputData == inputData:
            return i
        # if sampleI == 117440: print("2024:", outputData, "|", sampleInputData)
        i += 1
    """
    
    return -1

answer1 = part1()
answer2 = part2()
# print(answer1, answer2)