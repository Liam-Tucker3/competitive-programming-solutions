long_str = input()
short_str = ''
last_hyphen = True
for i in range(len(long_str)):
  this_char = long_str[i]
  if (last_hyphen):
    last_hyphen = False
    short_str += this_char
  if (this_char == '-'):
    last_hyphen = True
print(short_str)
