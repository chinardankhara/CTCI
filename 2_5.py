#same reference code as 2.1
#havent got the time to test. need to come back to this later
def sum_lists(head1, head2):
  curr1, curr2, carry = head1, head2, 0
  head3 = Node(None)
  curr3 = head3
  while curr1 != None and curr2 != None:
    curr3.set_data((curr1.get_data() + curr2.get_data + carry) % 10)
    curr3.set_next(Node(None))
    curr3 = curr3.get_next()
    carry = (curr1.get_data() + curr2.get_data() + carry) // 10
    curr1 = curr1.get_next()
    curr2 = curr2.get_next()

  if curr1 != None:
    while curr1 != None: 
      curr3.set_next(Node((carry + curr1.get_data()) % 10))
      carry = (curr1.get_data() + carry) // 10
      curr3.set_next(Node(None))
      curr3 = curr3.get_next()
      curr1 = curr1.get_next()
  elif curr2 != None:
    while curr2 != None: 
      curr3.set_next(Node((carry + curr2.get_data()) % 10))
      carry = (curr2.get_data() + carry) // 10
      curr3.set_next(Node(None))
      curr3 = curr3.get_next()
      curr2 = curr2.get_next()
  else:
    curr3.set_next(Node(carry))
    curr3 = curr3.get_next()

  return head3

#probably O(m + n) time and O(m) space where m and n are lists of lengths of given lists and m > n