`program = input
import sys
cset = program.split("")
cset2 = cset
forbiddencharacters = [] #where all the alphabetics go
for i in range(52):
  if i // 26:
    forbiddencharacters.append(chr(i + 71))
  else:
    forbiddencharacters.append(chr(i + 65))
stringmode = listmode = setmode = tuplemode = conditionalmode = functionmode = commentmode = variablemode = numbermode = False
characterlist1 = 
"""
¶ 
"""
# Things that will make my life easier
def findThisList(item, li):
  return [i for i in range(len(li)) if li[i] == item]
def findThisString(ch, s):
  return [i for i, ltr in enumerate(s) if ltr == ch]
def find(item, string): # This will actually be a helper function for a command called [insert here]
  li = []
  try:
    li = findthisList(item, list(code.split()))
  except Exception as e:
    li = findthisString(item, str(code))
  
def flagThis(code, characters, flags):
  li = []
  for chr in characters:
    li += find(chr, code)
  for i1 in li:
    for i2 in i1:
      code[i2] = [code[i2], flags[li.index(i1)]]
  return code

   
      
  
  for chr in code:
    if chr in characters:
      
      
  

def run(thisCode):  
  for chr in thisCode:
    if chr in forbiddencharacters and not stringmode and not commentmode:
      print("Error: alphanumeric characters detected outside of a string or comment.")
      sys.exit()
   
  
    








































































































































































































































































































`
