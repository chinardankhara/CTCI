#refernence code
#write a  class for linkedlist and node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
    
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
class LinkedList:
    #initialize the head
    def __init__(self):
        self.head = None

#actual problem
def remove_dups(head):
  buffer = set()
  buffer.add(head.get_data())
  point1 = head
  point2 = head.get_next()
  repeat = False
  
  while point2.get_next() is not None and (repeat):
    if point2.get_next() is None: repeat = True
    if point2.get_data() in buffer:
      point1.set_next(point2.get_next())
      point2 = point2.get_next()
    else:
      buffer.add(point2.get_data())
      point2 = point2.get_next()
      point1 = point1.get_next()

#a little hacky solution instead of dealing with a single pointer logic. I am too tired. O(n), O(n)