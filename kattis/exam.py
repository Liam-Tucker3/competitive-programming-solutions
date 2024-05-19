# Problem D
n = int(input())
me = input()
you = input()

score = 0
friend_right = n
friend_wrong = len(me) - n

for i in range(len(me)):
    if me[i] == you[i] and friend_right > 0:
        friend_right -= 1
        score += 1
    elif me[i] != you[i] and friend_wrong > 0:
        friend_wrong -= 1
        score += 1
print(score)