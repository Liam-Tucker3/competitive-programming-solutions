# Importing useful function
from utils import readFile
# from sympy import symbols, Eq, solve, Minimize, S
# from sympy.solvers.inequalities import reduce_rational_inequalities

def part1():
    data = readFile('inputs/day13.txt')

    tokenCount = 0
    for i in range(0, len(data), 4):
        # Getting useful values
        l1 = data[i].split(' ')
        a = int(l1[2][:-1].split('+')[1])
        c = int(l1[3].split('+')[1])
        l2 = data[i+1].split(' ')
        b = int(l2[2][:-1].split('+')[1])
        d = int(l2[3].split('+')[1])
        l3 = data[i+2].split(' ')
        e = int(l3[1][:-1].split('=')[1])
        f = int(l3[2].split('=')[1])

        determinant = a * d - b * c

        if determinant == 0: print("Det=0:", i, a, b, c, d, e, f)

        # Apply Cramer's Rule to solve for x and y
        x = (e * d - b * f) / determinant
        y = (a * f - e * c) / determinant
        if int(x) - x > 0.001 or int(x) - x < -0.001: continue # No int solution
        if int(y) - y > 0.001 or int(y) - y < -0.001: continue # No int solution
        x, y = int(x), int(y)

        tokenCount += 3*x + y
    
    return tokenCount


def part2():
    data = readFile('inputs/day13.txt')

    tokenCount = 0
    for i in range(0, len(data), 4):
        # Getting useful values
        l1 = data[i].split(' ')
        a = int(l1[2][:-1].split('+')[1])
        c = int(l1[3].split('+')[1])
        l2 = data[i+1].split(' ')
        b = int(l2[2][:-1].split('+')[1])
        d = int(l2[3].split('+')[1])
        l3 = data[i+2].split(' ')
        e = int(l3[1][:-1].split('=')[1]) + 10000000000000
        f = int(l3[2].split('=')[1]) + 10000000000000

        determinant = a * d - b * c

        if determinant == 0: print("Det=0:", i, a, b, c, d, e, f)

        # Apply Cramer's Rule to solve for x and y
        x = (e * d - b * f) / determinant
        y = (a * f - e * c) / determinant
        if int(x) - x > 0.001 or int(x) - x < -0.001: continue # No int solution
        if int(y) - y > 0.001 or int(y) - y < -0.001: continue # No int solution
        x, y = int(x), int(y)

        tokenCount += 3*x + y
    
    return tokenCount

answer1 = part1()
answer2 = part2()
print(answer1, answer2)