# Importing useful function
from utils import readFile, toGrid, printGrid

def part1():
    # Splitting data into inputs, connections
    data = readFile('inputs/day24.txt')
    i = 0
    while data[i] != "": i += 1
    inputData = data[:i]
    connectionsData = data[i+1:]

    # Parsing inputs
    inputs = {}
    for line in inputData:
        vals = line.split(": ")
        inputs[vals[0]] = int(vals[1])

    # Parsing connections
    connections = []
    for line in connectionsData:
        vals = line.split(" ")
        connections.append([vals[0], vals[2], vals[1], vals[4]])

    # Updating all values
    while True:
        i = 0
        while i < len(connections):
            vals = connections[i]
            
            # Skipping if we don't have both inputs yet
            if vals[0] not in inputs.keys() or vals[1] not in inputs.keys(): 
                i += 1
                continue # Don't have inputs yet

            # Adding new value to connections
            if vals[2] == "AND": inputs[vals[3]] = inputs[vals[0]] & inputs[vals[1]] # AND
            elif vals[2] == "OR": inputs[vals[3]] = inputs[vals[0]] | inputs[vals[1]] # OR
            elif vals[2] == "XOR": inputs[vals[3]] = inputs[vals[0]] ^ inputs[vals[1]] # XOR
            else: print("ERROR", vals)

            # Removing this connection from list
            connections = connections[:i] + connections[i+1:]

        # End of inner while
        if len(connections) == 0: break

    # End of outer while
    outputDecVal = 0
    for i in range(10): outputDecVal += inputs[f"z0{i}"] * 2**(i)
    for i in range(10, 46): outputDecVal += inputs[f"z{i}"] * 2**(i)

    return outputDecVal

def part2():
    # Splitting data into inputs, connections
    data = readFile('inputs/day24.txt')
    i = 0
    while data[i] != "": i += 1
    inputData = data[:i]
    connectionsData = data[i+1:]

    # Parsing inputs
    inputs = {}
    for line in inputData:
        vals = line.split(": ")
        inputs[vals[0]] = vals[0]

    # Parsing connections
    connections = []
    for line in connectionsData:
        vals = line.split(" ")
        connections.append([vals[0], vals[2], vals[1], vals[4]])

    # Updating all values
    while True:
        i = 0
        while i < len(connections):
            vals = connections[i]
            
            # Skipping if we don't have both inputs yet
            if vals[0] not in inputs.keys() or vals[1] not in inputs.keys(): 
                i += 1
                continue # Don't have inputs yet

            # Adding new value to connections
            if vals[2] == "AND": inputs[vals[3]] = f"({inputs[vals[0]]} AND {inputs[vals[1]]})" # AND
            elif vals[2] == "OR": inputs[vals[3]] = f"({inputs[vals[0]]} OR {inputs[vals[1]]})" # OR
            elif vals[2] == "XOR": inputs[vals[3]] = f"({inputs[vals[0]]} XOR {inputs[vals[1]]})" # XOR
            else: print("ERROR", vals)

            # Removing this connection from list
            connections = connections[:i] + connections[i+1:]

        # End of inner while
        if len(connections) == 0: break

    # End of outer while
    outputDecVal = 0
    for i in range(10): print(f"z0{i} = {inputs[f'z0{i}']}")
    for i in range(10, 46): print(f"z{i} = {inputs[f'z{i}']}")

    return outputDecVal

answer1 = part1()
answer2 = part2()
print(answer1, answer2)