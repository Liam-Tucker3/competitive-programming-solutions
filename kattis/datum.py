# Datum

# Getting input
vals = input().split()
date = int(vals[0])
month = int(vals[1])

daysOfWeek = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"] # Thursday first based on provided input
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, len(daysInMonth)):
    daysInMonth[i] += daysInMonth[i-1] # Getting cumulative number of 

daysIntoYear = 0
if month != 1: daysIntoYear += daysInMonth[month - 2]
daysIntoYear += date
daysIntoYear -= 1 # Because the first date was a Thursday

print(daysOfWeek[daysIntoYear % 7])

