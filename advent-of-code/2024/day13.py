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

        # TODO: Calculate  values

        # Define equations
        v1, v2 = symbols('v1 v2')
        eq1 = Eq(ax * v1 + bx * v2, cx)
        eq2 = Eq(ay * v1 + by * v2, cy)

        # Solve the system of equations for v1 and v2
        solutions = solve([eq1, eq2], (v1, v2), dict=True)

        # Define the objective function
        objective = 3 * v1 + v2

        # Find the solution that minimizes the objective
        min_value = S.Infinity
        best_solution = None

        for solution in solutions:
            # Substitute the solution into the objective function
            objective_value = objective.subs(solution)
            if objective_value < min_value:
                min_value = objective_value
                best_solution = solution

        # Output the best solution and the minimized value
        print("Best Solution:", best_solution)
        print("Minimum Value of Objective Function:", min_value)






    return 0

def part2():
    data = readFile('inputs/day13.txt')

    return 2

answer1 = part1()
answer2 = part2()
print(answer1, answer2)