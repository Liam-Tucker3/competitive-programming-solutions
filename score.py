# Score!
n = int(input())
lines = []
for i in range(n):
    lines.append(input())
    
HScore = 0
AScore = 0
HLead = 0
ALead = 0

currLead = "T"
leadChangeTime = "X"

line1 = lines[0].split()
ch = line1[0]
score = int(line1[1])
firstTime = line1[2].split(':')
seconds = 60*int(firstTime[0]) + int(firstTime[1])
if ch == "H":
    HScore += score
    currLead = "H"
    leadChangeTime = seconds
else:
    AScore = score
    currLead = "A"
    leadChangeTime = seconds
    
for line in lines[1:]:
    l = line.split()
    thisTeam = l[0]
    thisScore = int(l[1])
    thisTime = l[2].split(':')
    thisSeconds = 60*int(thisTime[0]) + int(thisTime[1])
    
    """
    print("Current Score H/A: ", HScore, AScore)
    print("Cumulative Lead H/A: ", HLead, ALead)
    print("Current Lead/Last Lead Change: ", currLead, leadChangeTime)
    print("This Team/Score/Seconds", thisTeam, thisScore, thisSeconds)
    """
    
    # Updating Scores
    if thisTeam == "H": HScore += thisScore
    if thisTeam == "A": AScore += thisScore
        
    # Case where the game was tied
    if currLead == "T": 
        currLead = thisTeam
        leadChangeTime = thisSeconds
    
    # Case where game is now tied
    elif AScore == HScore:
        timeLastLead = thisSeconds - leadChangeTime
        if thisTeam == "H": ALead += timeLastLead
        else: HLead += timeLastLead
            
        leadChangeTime = thisSeconds
        currLead = "T"
        
    # Case where lead changed from A to H
    elif currLead == "A" and HScore > AScore:
        timeLastLead = thisSeconds - leadChangeTime
        ALead += timeLastLead
        leadChangeTime = thisSeconds
        currLead = "H"
        
    # Case where lead changed from A to H
    elif currLead == "H" and HScore < AScore:
        timeLastLead = thisSeconds - leadChangeTime
        HLead += timeLastLead
        leadChangeTime = thisSeconds
        currLead = "A"

# End of game
thisWinner = currLead
assert currLead == "H" or currLead == "A"
if thisWinner == "A": ALead += 60 * 32 - leadChangeTime
if thisWinner == "H": HLead += 60 * 32 - leadChangeTime

# Determining time home team led
HMins = int(HLead / 60)
HSeconds = str(int(HLead - 60 * HMins))
HMins = str(HMins)
# if len(HMins) == 1: HMins = f"0{HMins}"
if len(HSeconds) == 1: HSeconds = f"0{HSeconds}"
    
# Determining time away team led
AMins = int(ALead / 60)
ASeconds = str(int(ALead - 60 * AMins))
AMins = str(AMins)
# if len(AMins) == 1: AMins = f"0{AMins}"
if len(ASeconds) == 1: ASeconds = f"0{ASeconds}"
    
# printing results
print(f"{thisWinner} {HMins}:{HSeconds} {AMins}:{ASeconds}")
