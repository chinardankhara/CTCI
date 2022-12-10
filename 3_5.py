def sort_stack(s):
  r = Stack()

  while s.size() != 0:
    temp = s.pop()
    while r.size() != 0 and temp > r.peek():
      s.push(r.pop())
    r.push(temp)

  while r.size() != 0:
    s.push(r.pop())

  return s