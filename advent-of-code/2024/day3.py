# Importing useful function
from utils import readFile

def part1():
    
    # Helper functions
    def isDigit(ch):
        if ch == "0" or ch == "1" or ch == "2" or ch == "3" or ch == "4": return True
        if ch == "5" or ch == "6" or ch == "7" or ch == "8" or ch == "9": return True
        return False

    # Reading data
    data = readFile('inputs/day3.txt')

    sum = 0

    # Iterating through each line
    for line in data:
        i = 0
        v1 = 0
        v2 = 0
        while i < len(line): # Avoiding out-of-bounds
            if i+4 < len(line) and line[i:i+4] == "mul(": # Potential mul
                i += 4
                j = i
                while j < len(line) and isDigit(line[j]): j += 1
                if j != i: # Found a first number:
                    v1 = int(line[i:j])
                    i = j
                    if line[i] == ",": # Found comma
                        i += 1
                        j = i
                        while j < len(line) and isDigit(line[j]): j += 1
                        if j != 1: # Found a second number:
                            v2 = int(line[i:j])
                            i = j
                            if line[i] == ")": # Finished mul command
                                i += 1
                                sum += v1 * v2
                                v1 = 0
                                v2 = 0

                pass
            else:
                i += 1

    # End of for loop
    return sum


# Very inefficient solution
def part2():
    
    # Helper functions
    def isDigit(ch):
        if ch == "0" or ch == "1" or ch == "2" or ch == "3" or ch == "4": return True
        if ch == "5" or ch == "6" or ch == "7" or ch == "8" or ch == "9": return True
        return False
    
    def isDo(ch):
        return ch == "do()"
    
    def isDont(ch):
        return ch == "don't()"


    # Reading data
    data = readFile('inputs/day3.txt')

    sum = 0

    do = True

    # Iterating through each line
    for line in data:
        i = 0
        v1 = 0
        v2 = 0

        while i < len(line): # Avoiding out-of-bounds
            if not do: # No need to check for mul commands
                if i + 4 < len(line) and isDo(line[i:i+4]):
                    do = True
                    i += 4
                    continue
                else:
                    i += 1
                    continue

            if i+4 < len(line) and line[i:i+4] == "mul(": # Potential mul
                i += 4
                j = i
                while j < len(line) and isDigit(line[j]): j += 1
                if j != i: # Found a first number:
                    v1 = int(line[i:j])
                    i = j
                    if line[i] == ",": # Found comma
                        i += 1
                        j = i
                        while j < len(line) and isDigit(line[j]): j += 1
                        if j != 1: # Found a second number:
                            v2 = int(line[i:j])
                            i = j
                            if line[i] == ")": # Finished mul command
                                i += 1
                                sum += v1 * v2
                                v1 = 0
                                v2 = 0

                pass
            elif i+7 < len(line) and isDont(line[i:i+7]):
                do = False
                i += 7
                continue
            else:
                i += 1
                continue

    # End of for loop
    return sum

answer1 = part1()
answer2 = part2()
print(answer1, answer2)