#reference code same as 2_1

def remove_k_from_last(head, k):
  p1 = p2 = head
  for i in range(k):
    p2 = p2.get_next()

  while p2.get_next() is not None:
    p2 = p2.get_next()
    p1 = p1.get_next()

  return p1.get_data()

#O(n) time, O(1) memory