# print(87178291200 * 15)

successes = {}
successes[1] = 1
num = int(input())
maxNum = 1
while (num != 0):
  if (num in successes.keys()):
    val = successes[num]
    print(int(val % 10))
    num = int(input())
    continue
  val = successes[maxNum]
  for j in range(maxNum + 1, num + 1):
    # print("start", val)
    val = val * j
    # print(val)
    while val % 10 == 0:
      # print(j, val)
      val = int(val / 10)
    val = val % 1000000
    successes[j] = val

  maxNum = max(maxNum, num)
  # print("new max num", maxNum)
  print(int(val % 10))
  num = int(input())