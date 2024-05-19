def checkValid(i, myGraph, vertexList):
  this_poss = myGraph[i]
  this_match = []
  for j in range(len(this_poss)):
    if this_poss[j] == 1: this_match.append(j)
  for xind in range(len(this_match)):
    for yind in range(0, xind):
      x = this_match[xind]
      y = this_match[yind]
      if x == y or x == i or y == i: continue
      if myGraph[x][y] == 1 and myGraph[y][x] == 1:
        vertexList.remove(i)
        if x in vertexList: vertexList.remove(x)
        if y in vertexList: vertexList.remove(y)
        return vertexList
  return vertexList


n = int(input())
while (n != -1):
  vertexList = []
  myGraph = []
  for i in range(n):
    this_list = input().split()
    for j in range(len(this_list)):
      this_list[j] = int(this_list[j])
    myGraph.append(this_list)
    vertexList.append(i)

  # Loooping through vertex list
  initialSize = len(vertexList)
  for i in range(initialSize):
    if i in vertexList:
      vertexList = checkValid(i, myGraph, vertexList)

  outputstr = ""
  for i in range(len(vertexList)):
    outputstr += str(vertexList[i])
    outputstr += " "
  print(outputstr[:-1])
  n = int(input())
