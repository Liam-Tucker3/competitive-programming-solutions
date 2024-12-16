# Importing useful function
from utils import readFile
from sympy import symbols, Eq, solve, Minimize, S
from sympy.solvers.inequalities import reduce_rational_inequalities

def part1():
    data = readFile('inputs/day13.txt')
    tokenCount = 0
    for i in range(0, len(data), 4):
        # Getting useful values
        l1 = data[i].split(' ')
        ax = int(l1[2].split('+')[1])
        ay = int(l1[3].split('+')[1])
        l2 = data[i+1].split(' ')
        bx = int(l2[2].split('+')[1])
        by = int(l2[3].split('+')[1])
        l3 = data[i+2].split(' ')
        cx = int(l3[1].split('=')[1])
        cy = int(l3[2].split('=')[1])

        # TODO: Calculate  



    return 0

def part2():
    data = readFile('inputs/dayX.txt')

    return 2

answer1 = part1()
answer2 = part2()
print(answer1, answer2)