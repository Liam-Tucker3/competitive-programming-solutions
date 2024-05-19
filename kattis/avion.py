outputstr = ""

inputstr = []
for i in range(5):
  inputstr.append(input())
for i in range(5):
  thisstr = inputstr[i]
  if "FBI" in thisstr:
    thisoutputstr = str(i + 1) + " "
    outputstr += thisoutputstr
if outputstr == "": print("HE GOT AWAY!")
else:
  outputstr = outputstr[:-1]
  print(outputstr)
