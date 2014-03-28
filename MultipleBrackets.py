def MultipleBrackets(str): 

  # code goes here
  stack = []
  matches = 0
  for letter in str:
    if letter in "([":
      stack.append(letter)
    elif lett er in ")]" and len(stack) != 0:
      popped = stack.pop()
      if letter == ")" and popped == "(":
        matches += 1
        continue
      elif letter == "]" and popped == "[":
        matches += 1
        continue
      else:
        return 0
    elif letter in ")]" and len(stack) == 0:
      return 0
  if len(stack) == 0:
    return "%d %d" %(1, matches) 
  else:
    return 0
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print MultipleBrackets("[]")  

