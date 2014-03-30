def LetterCount(str): 
  repeating_count = 0
  to_return = ""
  str_arr = str.split()
  repeating_count = 0
  for word in str_arr:
    repeating_dict = {}
    is_changed = False
    for i in range(0, len(word)):
      letter = word[i]
      if letter not in repeating_dict:
        repeating_dict[letter] = 1
      else:
        repeating_dict[letter] += 1
    for count in repeating_dict.values():
      if count > repeating_count:
        is_changed = True
        repeating_count = count

    if is_changed and repeating_count != 1:
      to_return = word
  if not is_changed and repeating_count == 1:
    return -1
  return to_return
print LetterCount("hello apple pie")
print LetterCount("No Words")