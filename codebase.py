import random
insults = open("insults.txt" , "r")
content = insults.readlines()
num = len(contents)
def insulting() -> str:
  '''Returns an insult to the user'''
  insult_number = rand(0,num)
  return content[num].strip()
