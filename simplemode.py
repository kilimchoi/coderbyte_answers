def SimpleMode(arr): 

  # code goes here
  dict = {}
  for n in arr:
    if n not in dict:
      dict[n] = 1
    else:
      dict[n] += 1


  sorted_dict = sorted(dict.items(), key=lambda x: x[1])

  #check if all values are equal
  to_return, max_so_far = 0, 0
  first_key, first_val = sorted_dict[0][0], sorted_dict[0][1]
  max_list, smallest_index = [], len(arr)
  is_equal = False
  for tup in sorted_dict:
    if tup[1] > max_so_far and tup[1] != first_val:
      to_return, max_so_far = tup[0], tup[1]
      is_equal = False
    elif tup[1] == max_so_far:
      max_list.append(tup[0])
    elif tup[1] == first_val:
      is_equal = True
  if len(sorted_dict) == 1 or is_equal:
    return -1
  else:
    for max_n in max_list:
      if arr.index(max_n) < smallest_index:
        smallest_index = arr.index(max_n)
    if arr.index(to_return) < smallest_index:
      return to_return
    else:
      return arr[smallest_index]

print SimpleMode([5, 5, 5, 5])
print SimpleMode([5, 10, 10, 6, 5])
print SimpleMode([10, 4, 5, 2, 4])
print SimpleMode([1, 2, 3, 100])