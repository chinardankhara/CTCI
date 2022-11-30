#reference code same as 2_1

#returns head of the new partition list. O(n) space and time
def partition(head, k):
  temp = LinkedList(None, None)
  curr = head
  while curr.get_next() is not None:
    if curr.get_data()  < k:
      temp.head = Node(curr.get_data(), temp.head)
    else: 
      temp.tail.set_next(Node(curr.get_data(), None))
  return temp.head