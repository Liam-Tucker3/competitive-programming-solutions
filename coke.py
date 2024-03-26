""" Coke.py NO DP"""

## """ Buying Coke -- Wrong Answer"""
testCases = int(input())
for i in range(testCases):
    vals = input().split()
    c = int(vals[0])
    ones = int(vals[1])
    five = int(vals[2])
    tens = int(vals[3])
    
    coinCount = 0
    
    if c > five + tens:
        # print("HERE")
        tenOne = c - (five+tens)
        tenOne = min(tenOne, int((ones + 2 * (tens - tenOne)) / 3), tens)
        # print(tenOne, tens)
        c -= tenOne
        tens -= tenOne
        ones -= 3*tenOne
        five += tenOne
        coinCount += 4 * tenOne
    
    """
    ## 10 1 1 1 -> 5
    if tens + five < c:
        tenOne = min(c - five - tens, tens, int(ones / 3))
        c -= tenOne
        tens -= tenOne
        ones -= 3*tenOne
        five += tenOne
        coinCount += tenOne
    """
    
    tenRuns = min(c, tens)
    coinCount += tenRuns
    c -= tenRuns
    tens -= tenRuns
    ones += 2 * tenRuns
    
    if c == 0:
        print(coinCount)
        continue
        
    assert tens == 0, c > 0
        
    doubleFive = 0
    if five >= 2*c: doubleFive = c
    elif c > five: doubleFive = 0
    else: doubleFive = five - c
    coinCount += 2 * doubleFive
    five -= 2 * doubleFive
    c -= doubleFive
    ones += 2 * doubleFive
    
    if c == 0:
        print(coinCount)
        continue
        
    assert c > 0
    
    fiveRuns = min(c, five)
    coinCount += 4 * fiveRuns
    c -= fiveRuns
    five -= fiveRuns
    ones -= 3* fiveRuns
    
    assert five == 0, c >= 0
    
    coinCount += 8 * c
    print(coinCount)