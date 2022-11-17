#O(n), O(n)
def are_permutations(a, b):
  if len(a) != len(b): return False
  c = {}
  c = {i:1 if i not in c else c[i]+1 for i in a}
  for i in b:
    if i not in c: return False
    elif c[i] <= 0: return False
    else: c[i] -= 1
  return True
