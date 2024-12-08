# Importing useful function
from utils import readFile
from itertools import product


def part1():
    def eval(nums, ops):
        # print(len(nums), len(ops))
        currVal = nums[0]
        for i in range(len(ops)):
            if ops[i] == "+": currVal += nums[i+1]
            else: currVal *= nums[i+1]
        return currVal

    data = readFile('inputs/day7.txt')

    count = 0
    chars = ["*", "+"]
    for line in data:
        vals = line.split(' ')
        target = vals[0][:-1]
        target = int(target)
        vals = vals[1:]
        for i in range(len(vals)): vals[i] = int(vals[i])

        perms = [''.join(p) for p in product(chars, repeat=len(vals)-1)]
        # print(perms)
        for p in perms:
            if eval(vals, p) == target:
                count += target
                break

    return count

def part2():
    def eval(nums, ops):
        # print(len(nums), len(ops))
        currVal = nums[0]
        for i in range(len(ops)):
            if ops[i] == "+": currVal += nums[i+1]
            elif ops[i] == "*": currVal *= nums[i+1]
            else: currVal = int(str(currVal) + str(nums[i+1]))
        return currVal

    data = readFile('inputs/day7.txt')

    count = 0
    chars = ["*", "+", '|']
    x = 0
    for line in data:

        vals = line.split(' ')
        target = vals[0][:-1]
        target = int(target)
        vals = vals[1:]
        for i in range(len(vals)): vals[i] = int(vals[i])

        perms = [''.join(p) for p in product(chars, repeat=len(vals)-1)]
        # print(perms)
        for p in perms:
            if eval(vals, p) == target:
                count += target
                break

    return count


answer1 = part1()
answer2 = part2()
print(answer1, answer2)