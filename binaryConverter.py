def BinaryConverter(str): 
  print str
  # code goes here
  result, factor = 0, 1
  for i in range(len(str) - 1, -1, -1):
  	result += int(str[i]) * factor
  	factor *= 2
  return result
# keep this function call here  
# to see how to enter arguments in Python scroll down
print BinaryConverter("11")  