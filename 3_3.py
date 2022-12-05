class SetOfStacks:
  def __init__(self, threshold):
    self.map = {}
    self.threshold = threshold
    self.currkey = 0
    map[0] = Stack()
  
  def push(self, data):
    if self.map[self.currkey].size() < self.threshold:
      self.map[self.currkey].push(data)
    else:
      self.currkey += 1
      self.map[self.currkey] = Stack()
      self.map[self.currkey].push(data)

  def pop(self):
    temp = self.map[self.currkey].pop()
    if self.map[self.currkey].size() == 0:
      del self.map[self.currkey]
      self.currkey -= 1
    return temp

  def popAtIndex(self, index):
    if index in self.map.keys():
      temp = self.map[index].pop()
      if self.map[index].size() == 0:
        del self.map[index]
      return temp

#for all actions, behaves like a regular stack with O(1) ops
      
  