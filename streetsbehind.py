t = int(input())
for i in range(t):
    vals = input().split()
    n = int(vals[0])
    k = int(vals[1])
    a = int(vals[2])
    b = int(vals[3])

    serious = n
    casual = k

    if serious/(serious+1) < a/b:
        print(-1)
        continue
    
    steps = 0
    while 0 < casual:
        # print(steps+1, k, n)
        inc = int((serious*b - serious*a)/a)

        
        stepFactor = 0
        while (serious + (inc) * (2**stepFactor - 1)) / (serious + inc * (2**stepFactor-1)  + (inc+1)) < a/b and (serious + inc * (2**stepFactor-1)  + (inc+1)) < serious + casual:
            # print("StepFactor", stepFactor, "Num", k + (inc) * (2**stepFactor - 1), "Den", (k + inc * (2**stepFactor-1)  + (inc+1)))
            stepFactor += 1

        stepFactor = max(stepFactor-1, 1)
        steps += 2**stepFactor - 1
        serious += inc* (2**stepFactor - 1)
        casual -= inc* (2**stepFactor - 1)
        

        # steps += 1
        # k += inc

    print(steps)

"""
t = int(input())
for i in range(t):
    vals = input().split()
    n = int(vals[0])
    k = int(vals[1])
    a = int(vals[2])
    b = int(vals[3])

    serious = n
    casual = k
    n = serious + casual
    k = serious

    if k/(k+1) < a/b:
        print(-1)
        continue
    
    steps = 0
    while k < n:
        # print(steps+1, k, n)
        inc = int((k*b - k*a)/a)

        
        stepFactor = 0
        while (k + (inc) * (2**stepFactor - 1)) / (k + inc * (2**stepFactor-1)  + (inc+1)) < a/b and (k + inc * (2**stepFactor-1)  + (inc+1)) < n:
            # print("StepFactor", stepFactor, "Num", k + (inc) * (2**stepFactor - 1), "Den", (k + inc * (2**stepFactor-1)  + (inc+1)))
            stepFactor += 1

        stepFactor = max(stepFactor-1, 1)
        steps += 2**stepFactor - 1
        k += inc* (2**stepFactor - 1)
        

        # steps += 1
        # k += inc

    print(steps)
"""