""" Keylogger """
soundDict = {"clank": "a", 
             "bong": 'b', 
             "click": "c",
             "tap": "d",
             "poing": "e",
             "clonk": "f",
             "clack": "g",
             "ping": "h",
             "tip": "i",
             "cloing": "j",
             "tic": "k",
             "cling": "l",
             "bing": "m",
             "pong": "n",
             "clang": "o",
             "pang": "p",
             "clong": "q",
             "tac": "r",
             "boing": "s",
             "boink": "t",
             "cloink": "u",
             "rattle": "v",
             "clock": "w",
             "toc": "x",
             "clink": "y",
             "tuc": "z",
             "whack": "SPACE",
             "bump": "CAPS",
             "pop": "DEL",
             "dink": "SHIFTON",
             "thumb": "SHIFTOFF"}

n = int(input())
outputList = []

caps = False
shift = False

for i in range(n):
    sound = input()
    ch = soundDict[sound]
    
    # Cases where it's not a letter
    if ch == "SPACE": outputList.append(' ')
    elif ch == "CAPS": caps = not caps
    elif ch == "DEL":
        if len(outputList) >= 1: outputList.pop()
    elif ch == "SHIFTON": shift = True
    elif ch == "SHIFTOFF": shift = False
        
    # Case where it is a letter
    else:
        if caps != shift: ch = ch.upper()
        outputList.append(ch)
        
print(''.join(outputList))