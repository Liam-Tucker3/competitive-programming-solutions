# Problem B: No Duplicates
phrase = input().split(' ')
words = {}
noRepeats = "yes"
for p in phrase:
    if p in words.keys():
        noRepeats = "no"
    else:
        words[p] = 1

print(noRepeats)
