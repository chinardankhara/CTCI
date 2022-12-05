class stackMin:
  def __init__(self):
    self.stack = []

  def push(self, data):
    minimum = min(data, self.stack[-1][1])
    self.stack.append((data, minimum))

  def pop(self):
    return stack.pop()[0]

  def min(self):
    return stack.peek()[1]