""" Eb Alto Saxophone Player """
notes = {'c': [2, 3, 4, 7, 8, 9, 10],
         'd': [2, 3, 4, 7, 8, 9],
         'e': [2, 3, 4, 7, 8],
         'f': [2, 3, 4, 7],
         'g': [2, 3, 4],
         'a': [2, 3],
         'b': [2],
         'C': [3],
         'D': [1, 2, 3, 4, 7, 8, 9],
         'E': [1, 2, 3, 4, 7, 8],
         'F': [1, 2, 3, 4, 7],
         'G': [1, 2, 3, 4],
         'A': [1, 2, 3],
         'B': [1,2]}

testCases = int(input())
for i in range(testCases):
    s = input()

    fingers = [0 for j in range(11)]
    presses = [0 for j in range(11)]
    
    for ch in s:
        f = notes[ch]
        for j in range(1,11):
            if j not in f: fingers[j] = 0
            if j in f:
                if fingers[j] != 1: 
                    presses[j] += 1
                    fingers[j] = 1
        
    for j in range(1,11):
        print(presses[j], end=" ")
    print()
                
            