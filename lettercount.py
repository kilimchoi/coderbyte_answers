def LetterCount(str): 
  str_arr = str.split()
  max_count, res = 1, -1
  for word in str_arr:
    c = 1
    for ch in word:
      n = word.count(ch)
      if n > c:
        c = n
    if c > max_count:
      max_count = c
      res = word
  return res
    
  return to_return
print LetterCount("hello apple pie")
print LetterCount("No Words")