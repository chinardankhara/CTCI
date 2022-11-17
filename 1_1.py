#bit vector to store lower case ascii characters
#O(n), O(1)
def str_unique_lowercase_ascii(s):
  check = 0
  for i in s:
    x = ord(i) - ord('a')
    if (check & (1 << x)) > 0: return False
    check |= (1 << x)
  return True

#set to store unique char. Works with anything
#O(n), O(n)
def str_unique_unicode(s):
  c = set()
  for i in s:
    if i in c: return False
    c.add(i)
  return True