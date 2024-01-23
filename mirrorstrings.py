# Problem E
vals = input().split()
lower = int(vals[0])
upper = int(vals[1])

running_score = 0
# if lower % 2 == 1: running_score running_score + 5 ** int((lower+1)/2) + 2 ** num_slots

two_exp = (2 ** int((lower)/2)) % 1000000007
five_exp = (5 ** int((lower)/2)) % 1000000007


for i in range(lower, upper+1):
    if i % 2 == 1: 
        two_exp = (two_exp * 2) % 1000000007
        five_exp = (five_exp * 5) % 1000000007
    
    running_score = (running_score + two_exp + five_exp) % 1000000007
    
    
    #num_slots = int((i+1)/2)
    #running_score = running_score + 5 ** num_slots + 2 ** num_slots
    #running_score = running_score % 1000000007

print(running_score)