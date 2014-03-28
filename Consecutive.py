import math, sys
def Consecutive(arr): 

  # code goes here
  min, max = sys.maxint, -sys.maxint - 1
  for n in arr:
    if n < min:
      min = n
    elif n > max:
      max = n
  if (min - max < 0):
    count = math.fabs(min- max) - 1 
  elif (min - max == 0):
    return 0
  else:
    count = min - max - 1 
  for n in arr:
    if n != max and n != min and n > min and n < max:
      count -= 1
  return int(count)
print Consecutive([0,3]) 