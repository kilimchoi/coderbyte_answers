def SimpleMode(arr): 

  # code goes here
  dict = {}
  for n in arr:
    if n not in dict:
      dict[n] = 1
    else:
      dict[n] += 1
  max_key, max_val = 0, 0
  for i in range(0, len(arr)):
    if (dict[arr[i]] > max_val):
      max_val = dict[arr[i]]
      max_key = arr[i]
  if max_val != 1:
    return max_key
  return -1

print SimpleMode([5, 5, 5, 5])
print SimpleMode([5, 10, 10, 6, 5])
print SimpleMode([10, 4, 5, 2, 4])
print SimpleMode([1, 2, 3, 100])
