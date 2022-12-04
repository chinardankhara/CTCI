#if we knew the size of list beforehand, this would get too boring. Let's do this without the size. 
#same reference code as 2_1
def palindrome(head1):
  slow, fast = head1, head1 #we are using the runner technique
  stack = []

  while (fast.get_next() is not None) or (fast.get_next().get_next() is not None):
    fast = fast.get_next().get_next()
    stack.append(slow.get_data())
    slow = slow.get_next()

  del fast
  if len(stack) % 2 != 0: del stack[-1]

  while (slow != None):
    slow = slow.get_next()
    temp = stack.pop(-1) #constant time because its the last element
    if temp == slow.get_data():
      continue
    else:
      return False

  return True

#O(n) time for a single traversal or the list using slow and half a traversal using fastt. O(n) space for storing half the list in a stack