# some prep work
import sys
sys.setrecursionlimit(2147483647) # if you're exceeding this you're in an infinite loop
l = len
program = input()
import sys
cset = program.split("")
cset2 = cset
forbiddencharacters = [] #where all the alphabetics go
for i in range(52):
  if i // 26:
    forbiddencharacters.append(chr(i + 71))
  else:
    forbiddencharacters.append(chr(i + 65))
stringmode = listmode = setmode = tuplemode = conditionalmode = functionmode = commentmode = variablemode = numbermode = skipflag = False
cp1 = ["\n" ", "!", "\"", "#", "$", "%", "\'", "(", ")", "*", "+", ",", "-", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "[", "/", "]", "^", "_", "`", "{", "|", "}", "~"] #the legal characters
# helper functions
def factorial(i):
  if i > 0:
    return i * factorial(i - 1)
  return 1
def mergesplit(li):
  if l(li) == 1:
    return li
  length = l(li)
  li1, li2 = li[:length], li[length:]
  return [li1, li2]
def mergejoin(li1, li2):
  li3 = [] 
  i, j = 0, 0
  for k in range(0, l(li1) + l(li2)):
    if i == l(li1):
      li3.append(li2[j])
    elif j == l(li2):
      li3.append(li1[i])
      i += 1
    elif li2[j] < li1[i]:
      li3.append(li2[j])
      j += 1
    else:
      li3.append(li1[i])
      i += 1
  return li3
def mergesort(li):
  length = l(li)
  s = 1
  while s < length:
    s+=s
    for pos in range(0, length, s):
      st = pos
      m = pos + int(s / 2)
      e = pos + s
      li1 = li[st:m]
      li2 = li[m:e] 
      li[st:e] = mergejoin(li1, li2)
  return li
# here's the string and the comment section
currentstring1 = currentitem1 = currentstring2 = currenitem2 = ""
index = 0
  
    









































































































































































































































































































