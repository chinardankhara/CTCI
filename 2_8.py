def intersection(head1):
  slow, fast = head1, head1

  while True:
    slow = slow.get_next()
    fast = fast.get_next().get_next()
    if slow == fast:
      break
    elif (slow == None) or (fast == None):
      return None
    #this will exist because either you reach end of list
    #or you intersect at a point in the loop

  slow = head1
  while slow != fast:
    slow = slow.get_next() 
    fast = fast.get_next().get_next()
  return slow


#same reference code as 2_1. O(n) time and O(1) space