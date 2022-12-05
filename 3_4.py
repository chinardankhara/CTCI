class MyQueue:
  def __init__(self):
    self.inbox = Stack()
    self.outbox = Stack()

  def push(self, data):
    self.inbox.push(data)

  def pop(self):
    if self.outbox.size() != 0:
      return self.outbox.pop()
    for i in range(self.inbox.size()):
      self.outbox.push(self.inbox.pop())


#O(1) push, amortized O(1) pop. O(1) memory