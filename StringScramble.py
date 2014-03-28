def StringScramble(str1,str2): 

  # code goes here
  dict = {}
  for letter in str1:
    if letter in dict:
      if dict[letter] > 0:
        dict[letter] += 1
    else:
      dict[letter] = 1
  for letter in str2:
    if letter in dict:
      if dict[letter] > 0:
        dict[letter] -= 1
      else:
        return "false"
    else:
      return "false"
  return "true"
  
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print StringScramble("cdoer", "coder")  

