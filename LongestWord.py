def LongestWord(sen): 
  new_sen = ''
  for x in sen:
    t = ord(x)
    if t == 32:
      new_sen += chr(t)
    elif not ((t < 65) or (t > 90 and t < 97)):
      new_sen += chr(t)
  top = 0
  best = ''
  for word in new_sen.split(' '):
    if len(word) > top:
      top = len(word)
      best = word
  return best
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())           
