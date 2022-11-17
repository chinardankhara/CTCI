#works for unicode. O(n), O(n)
def is_permutation_of_palindrome(s):
  c = {}
  for i in s:
    if i not in c: c[i] = 0
    c[i] += 1
  count = 0
  for i in c.values():
    if i % 2 != 0: count += 1
    if count > 1: return False
  return True

