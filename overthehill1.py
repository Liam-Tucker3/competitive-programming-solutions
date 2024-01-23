# Problem C

# Setting up dict
values = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J" : 9, "K": 10, "L": 11, "M": 12, "N": 13,
          "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25,
          "0": 26, "1": 27, "2": 28, "3": 29, "4": 30, "5": 31, "6": 32, "7": 33, "8": 34, "9": 35, " ": 36}

reverse_values = {}
for k, v in values.items():
    reverse_values[v] = k

# Getting encoding matrix
n = int(input())
matrix = []
for i in range(n):
    matrix.append(input().split())
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(matrix[i][j])
        
# Getting input string
str = input()
remaining = n - ( len(str) % n ) if len(str) % n != 0 else 0
for i in range(remaining):
    str = str + " "

    
# Getting encoded message
result = []
for i in range(int(len(str) / n)):
    chunk = str[n*i:n*(i+1)]
    
    for j in range(n):
        this_val = 0
        for k in range(n): # Doing matrix multiplication
            this_val += matrix[j][k] * values[chunk[k]]
        result.append(this_val % 37)

        
str = ""
for r in result:
    str = str + reverse_values[r]
print(str)
        
    
    