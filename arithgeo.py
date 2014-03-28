import math

def ArithGeo(arr): 

  # code goes here
  arithmetic = "Arithmetic"
  geometric = "Geometric"
  prev_diff = math.fabs(arr[0] - arr[1])
  prev_factor = max(arr[0], arr[1]) / min(arr[0], arr[1])
  is_geometric = False
  is_arithmetic = False
  for i in range(1, len(arr) - 1):
     diff = math.fabs(arr[i] - arr[i+1])
     factor = max(arr[i+1], arr[i]) / min(arr[i+1], arr[i])
     if (factor == prev_factor and factor != 0 and not is_arithmetic):
          prev_factor = factor
          is_geometric = True
     elif (diff == prev_diff and not is_geometric):
          prev_diff = diff
          is_arithmetic = True
     else:
          return -1
  if is_geometric:
    return geometric
  else:
    return arithmetic
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ArithGeo([1,2,3,4,5,10,20])  
