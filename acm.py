""" ACM Contest Scoring """

# Getting Input
lines = []
l = input()
while l != "-1":
    lines.append(l)
    l = input()
    
# Counting problems, time
problemsSolved = 0
totalTime = 0
attempts = {} # Stores incorrect submissions

for line in lines:
    vals = line.split()
    thisTime = int(vals[0])
    thisProblem = vals[1]
    thisCorrect = vals[2]
    
    # If correct
    if thisCorrect == "right":
        problemsSolved += 1
        totalTime += thisTime
        if thisProblem in attempts.keys(): totalTime += 20 * attempts[thisProblem] # Adding penalty time
            
    else:
        if thisProblem not in attempts.keys(): attempts[thisProblem] = 1
        else: attempts[thisProblem] += 1

# Printing output
print(problemsSolved, totalTime)