vals = input().split()
n = int(vals[0])
m = int(vals[1])
s = int(vals[2])
p = int(vals[3])
q = int(vals[4])

pages = {}
for i in range(p):
    item = int(input())
    thisPage = 1 + int((item-1) / m)

    if thisPage in pages.keys(): pages[thisPage][0].append(item)
    else: pages[thisPage] = [ [item], [] ]

#print(pages)

for i in range(q):
    item = int(input())
    thisPage = 1 + int((item-1) / m)
    #print(thisPage, pages.keys())
    if thisPage in pages.keys(): pages[thisPage][1].append(item)
    else: pages[thisPage] = [ [], [item] ]

if len(pages.keys()) > 0: initialMaxPages = max(pages.keys())

pagesToDelete = []
pageList = list(pages.keys())
for thisPage in pageList:
    l1 = pages[thisPage][0]
    l2 = pages[thisPage][1]
    l1Count = len(l1)
    l2Count = len(l2)
    for thisl1 in l1:
        if thisl1 in l2: 
            l1Count -= 1
            l2Count -= 1
    
    if l1Count == 0 and l2Count == 0:
        pagesToDelete.append(thisPage)

    """
    s1 = set(pages[thisPage][0])
    s2 = set(pages[thisPage][1])
    if s1==s2: 
        pagesToDelete.append(thisPage)
    """

for ptd in pagesToDelete: del pages[ptd]


pageList = pages.keys()
# print(pages.keys())
if len(pageList) == 0: print(0)
else:
    large = max(pageList)
    small = min(pageList)
    clicks = 0

    if large == s: clicks += abs(s - small)
    elif small == s: clicks += abs(large-s)
    elif large < s: clicks += abs(s-small)
    elif small > s: clicks += abs(large - s)
    else: 
        clicks += abs(large - small)
        if abs(large-s) >= abs(small-s): clicks += abs(small-s)
        else: clicks += abs(large-s)

    """
    if large >= s and small <= s:
        clicks += large - small
        clicks += min(large-s, s-small)
    elif large >= s:
        clicks += large - s
    else:
        clicks += s - small
    """

    # print(clicks)
    # print(pages)
    # print(pageList)

    for page in pageList:
        thisVals = pages[page]
        desired = thisVals[1]
        selected = thisVals[0]

        optA = 1 + len(desired)
        optB = 1 + (m - len(desired))

        if page == initialMaxPages:
            thisItemCount = n - m * (page - 1)
            optB = 1 + thisItemCount - len(desired)

        commonVals = 0
        for i in desired:
            if i in selected: commonVals += 1
        optC = len(desired) + len(selected) - (2 * commonVals)

        assert optA >= 0
        assert optB >= 0
        assert optC >= 0
        # print(optA, optB, optC)
        clicks += min(optA, optB, optC)

    assert type(clicks) == int
    assert clicks >= 0
    print(clicks)
