"""
I don't now the big O here.A list based solutin to keep counts and letters with careful arithmetic produces O(n) runtime and memory but I kept this (less efficient) solution because I like a more pythonic solution. 
"""

def compress_string(s):
  counts = {}
  for i in s:
    if i not in counts: counts[i] = 0
    counts[i] += 1
  if len(counts) * 2 >= len(s):
    return s
  else:
    l = ''.join(k for k in [''.join(str(j) for j in i) for i in counts.items()])
    return l

    