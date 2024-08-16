# deathtaxes.py

# Getting input
commands = []
thisLine = input()
while thisLine.split()[0] != "die":
    commands.append(thisLine.split())
    thisLine = input()
commands.append(thisLine.split())

numShares = 0
avePrice = 0

moneyLeft = 0

for commandList in commands:
    if commandList[0] == "buy":
        newShares = int(commandList[1])
        newPrice = int(commandList[2])
        if numShares == 0 and avePrice == 0:
            numShares = newShares
            avePrice = newPrice
        else: 
            avePrice = (numShares * avePrice + newShares * newPrice) / (newShares + numShares)
            numShares += newShares
    if commandList[0] == "sell":
        newShares = int(commandList[1])
        newPrice = int(commandList[2])
        # avePrice = (numShares * avePrice - newShares * newPrice) / (numShares - newShares)
        numShares -= newShares
    if commandList[0] == "merge":
        shareRatio = int(commandList[1])
        numShares -= (numShares % shareRatio)
        avePrice *= shareRatio
        numShares /= shareRatio
    if commandList[0] == "split":
        shareRatio = int(commandList[1])
        avePrice /= shareRatio
        numShares *= shareRatio
    if commandList[0] == "die": 
        finalPrice = int(commandList[1])
        if finalPrice > avePrice:
            moneyLeft = 0.7 * numShares * (finalPrice - avePrice) + numShares * avePrice
        else:
            moneyLeft = numShares * finalPrice
    
    # print(numShares, avePrice)

print(moneyLeft)

