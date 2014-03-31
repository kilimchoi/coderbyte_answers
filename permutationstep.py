import itertools
def PermutationStep(num): 
  
  # code goes here
  #return min(v for v in (int("".join(x)) for x in
    #itertools.permutations(str(num))) if v>num)
  if num < 10:
    return -1
  if num < 100:
    a, b = divmod(num, 10)
    if a >= b:
      return -1
    return b*10 + a
  
  a = str(num)
  b = PermutationStep(int(a[1:]))
  if b != -1:
    return int(a[0] + str(b))
  if a[0] == max(a):
    return -1
  
  n = a[0]
  a = sorted(a)
  for ch in a:
    if ch > n:
      n = ch
      a.remove(n)
  return int(n + ''.join(a))
print PermutationStep(123)
print PermutationStep(11121)
print PermutationStep(41352)
print PermutationStep(12453)
print PermutationStep(9)
print PermutationStep(44444444)
print PermutationStep(111)
