#O(n), O(1)
def urlify(s):
  s = list(s)
  for i in range(len(s)):
    if s[i] == ' ': s[i] = "%20"
  return ''.join(i for i in s)

print(urlify('Mr John Smith'))