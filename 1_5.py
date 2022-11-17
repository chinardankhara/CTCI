#checks if a replace operation can make the strings equal
def replace(a, b):
    cond = False
    for i in range(len(a)):
      if a[i] != b[i]:
        if cond: return False
        cond = True
    return True

#checks if an insert operation can make the strings equal
def insert(a, b):
  i1, i2 = 0, 0
  while ((i1 < len(a)) and (i2 < len(b))):
    if a[i1] != b[i2]:
      if i1 != i2:
        return False
      i2 += 1
    else:
      i1 += 1
      i2 += 1
  return True

#main function. O(n), O(1)
def one_edit_diff(a, b):
  if len(a) == len(b):
    return replace(a, b)
  elif len(a) + 1 == len(b):
    return insert(a, b)
  elif len(a) - 1 == len(b):
    return insert(b, a)
  return False
  
  