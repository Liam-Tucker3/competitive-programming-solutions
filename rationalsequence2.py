# Problem E
# Produces path as you go from bottom to top
def get_path(turns, p, q):
    if p == q:
        return turns
    elif p > q:
        my_turns = turns + "L"
        return get_path(my_turns, (p-q), q)
    else:
        my_turns = turns + "R"
        return get_path(my_turns, p, (q-p))

num_cases = int(input())
for i in range(num_cases):
    vals = input().split()
    case_num = vals[0]
    nums = vals[1].split('/')
    p = int(nums[0])
    q = int(nums[1])

    path = get_path("", p, q)
    score = 2 ** len(path)
    for j in range(len(path)):
        if path[j] == "L": score += 2 ** j
            
    print(case_num, score)
