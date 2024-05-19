import math

def func():

    text = input().split()
    m = int(text[0])
    n = int(text[1])
    t = int(text[2])

    if t == 7: # Case O(n)
        if n <= m:
            print("AC")
            return
        else:
            print("TLE")
            return
    if t == 6: # Case O(n lg2n)
        if math.log2(n) <= m/n:
            print("AC")
            return
        else:
            print("TLE")
            return
    if t == 5: # Case O(n^2)
        if n*n <= m:
            print("AC")
            return
        else: 
            print("TLE")
            return
    if t == 4: # Case O(n^3)
        if n*n*n <= m: 
            print("AC")
            return
        else: 
            print("TLE")
            return
    if t == 3: # Case O(n^4)
        if n*n*n*n <= m:
            print("AC")
            return
        else:
            print("TLE")
            return

    if t == 2: # Case O(2^n)
        if math.log2(m) >= n:
            print("AC")
            return
        else:
            print("TLE")
            return

    if t == 1: # Case O(n)
        if n > 20: 
            print("TLE")
            return
        for i in range(1,n+1):
            m = m / i
            if m < 1:
                print("TLE")
                return  
        print("AC")
        return
    
func()