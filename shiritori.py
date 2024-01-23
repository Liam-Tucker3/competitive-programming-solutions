from sys import stdin

n=int(input())
m = dict()
prev = str(input())

m[prev] = 1
loser = ""

for i in range(1, n):
    word = str(input())
    if (loser != ""):
        prev = word
        continue

    if (prev[-1] != word[0] or (word in m)):
        if (i%2):
            loser = "Player 2 lost"
        else:
            loser = "Player 1 lost"
    
    m[word] = 1
    prev = word


if (loser == ""):
    print("Fair Game")
else:
    print(loser)




