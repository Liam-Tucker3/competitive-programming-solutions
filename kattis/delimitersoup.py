# Problem G
good = True
stack = []
llen = int(input())
s = input()
for i in range(llen):
    ch = s[i]
    if ch == '(' or ch == '{' or ch == '[': stack.append(ch)
    if ch == ')':
        if len(stack) == 0 or stack[-1] != '(':
            print(ch, i)
            good = False
            break
        else: stack = stack[:-1]
    if ch == ']':
        if len(stack) == 0 or stack[-1] != '[':
            print(ch, i)
            good = False
            break
        else: stack = stack[:-1]
    if ch == '}':
        if len(stack) == 0 or stack[-1] != '{':
            print(ch, i)
            good = False
            break
        else: stack = stack[:-1]
            
if good:
    print("ok so far")