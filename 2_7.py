def intersection(head1, head2):
  #traverse through each list to find if there is an intersection
  curr1, curr2 = head1, head2
  size1, size2 = 1, 1
  while curr1.get_next() is not None:
    curr1 = curr1.get_next()
    size1 += 1
  while curr2.get_next() is not None:
    curr2 = curr2.get_next()
    size2 += 1

  if curr1 != curr2:
    return None

  #now we know there is an intersection, time to find it
  curr1, curr2 = head1, head2
  if size1 > size2:
    truncate = curr1
    other = curr2
  else:
    truncate = curr2
    other = curr1
  temp = max(size1, size2) - min(size1, size2)
  while temp > 0:
    truncate = truncate.get_next()

  while True: #since we have already checked presence of intersection, we dont need to set any checks here
    if truncate != other:
      truncate = truncate.get_next()
      other = other.get_next()
    else:
      return truncate

#note that the problem asks to return equality by reference, not value
#O(m + n) in time, O(1) in space
  