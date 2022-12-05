#reference code for the stack and queue questions

class Stack:
  def __init__(self):
    self.stack = []

  def pop(self):
    return self.pop(-1)

  def push(self, data):
    self.stack.append(data)

  def peek(self):
    return self.stack[-1]

  def size(self):
    return len(self.stack)

#for queue, we will use the inbuilt Queue class in collections package