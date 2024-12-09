# Importing useful function
from utils import readFile

def part1():
    data = readFile('inputs/day9.txt')[0] # Only one line
    # print(len(data))
    # print(data)

    # Converting data to array of ints
    newList = [-1 for i in range(len(data))]
    for i in range(len(data)): newList[i] = int(data[i]) # Converting to int
    data = newList
    # print(data)

    # Getting file system length
    fileSystemSize = 0
    for i in range(len(data)): fileSystemSize += data[i]

    # Creating file system
    fileSystem = ["." for i in range(fileSystemSize)]

    # Filling file system w/ starting values
    index = 0
    fileCount = 0
    for i in range(len(data)):
        thisSize = data[i]
        if i % 2 == 0:
            for j in range(thisSize):
                fileSystem[index+j] = fileCount
            fileCount += 1
        index += thisSize
    
    # print(fileSystem)

    # Filling open spaces
    l = 0
    u = len(fileSystem) - 1
    while l < u:
        # Iterating to find indices to swap
        if fileSystem[l] != ".":
            l += 1
            continue
        if fileSystem[u] == ".":
            u -= 1
            continue

        # Swapping indices
        fileSystem[l] = fileSystem[u]
        fileSystem[u] = "."
        l += 1
        u -= 1

    # print(fileSystem)
    
    # Counting checksum
    checksum = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] != ".": checksum += i * fileSystem[i]

    return checksum


def part2():
    data = readFile('inputs/day9.txt')[0] # Only one line
    # print(data)

    # Converting data to array of ints
    newList = [-1 for i in range(len(data))]
    for i in range(len(data)): newList[i] = int(data[i]) # Converting to int
    data = newList
    # print(data)

    # Getting file system length
    fileSystemSize = 0
    for i in range(len(data)): fileSystemSize += data[i]

    # Creating file system
    fileSystem = ["." for i in range(fileSystemSize)]

    # Filling file system w/ starting values
    index = 0
    fileCount = 0
    for i in range(len(data)):
        thisSize = data[i]
        if i % 2 == 0:
            for j in range(thisSize):
                fileSystem[index+j] = fileCount
            fileCount += 1
        index += thisSize
    
    # print(fileSystem)

    # Calculating initial offsets for all data
    offsets = [0 for i in range(len(data))]
    for i in range(1, len(data)): offsets[i] = offsets[i-1] + data[i-1]

    # Iterating through files from end to start
    i = len(data) - 1
    while i > 0:
        # Iterating through gaps from left to right
        j = 1
        while j < i:
            if data[i] > data[j]: # Cannot fit in gap
                j += 2
                continue
            else: # Fit in partial or full gap gap
                for k in range(offsets[j], offsets[j] + data[i]):
                    fileSystem[k] = int(i / 2) # Copying file indices to new location
                for k in range(offsets[i], offsets[i] + data[i]):
                    fileSystem[k] = "."
                # Updating offset, gap 

                offsets[j] += data[i]
                data[j] -= data[i]
            
            break
        i -= 2
        # End of inner while
    # End of outer while

    # Counting checksum
    checksum = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] != ".": checksum += i * fileSystem[i]

    return checksum

    """
    # Calculating gap sizes, offsets for gaps only
    gapSizes = [0 for i in range(int(len(data) / 2))]
    gapOffsets = [0 for i in range(int(len(data) / 2))]
    for i in range(int(len(data) / 2)):
        gapSizes[2*i + 1] = data[2*i + 1]
        gapOffsets[2*i + 1] = offsets[2*i + 1]

    # Attempting to move each file to the left
    for i in range(len(gapSizes)):
        pass
    """

answer1 = part1()
answer2 = part2()
print(answer1, answer2)