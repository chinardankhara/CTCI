#assuming a square array for simplicity, rectangular case
#is trivial. Just replace approapriate length numbers.
def set_zeros(n):
  #store if there are zeros in first row and column
  row_zero, col_zero = False, False
  for i in n[0]:
    if i == 0: row_zero = True
  for i in range(len(n)):
    if n[0][i] == 0: col_zero = True

  #iterate through rest of array and store zero info in first
  #row and column
  for i in range(1, len(n)):
    for j in range(1, len(n)):
      if n[i][j] == 0:
        n[i][0] = 0
        n[0][j] = 0


  #now its time to nullify the rows and columns
  for i in range(1, len(n)):
    if n[i][0] == 0: n[i] = 0
  for j in range(1, len(n)):
    if n[0][j] == 0:
      for i in range(1, len(n)):
        n[i][j] = 0

  if row_zero: n[0] = 0
  if col_zero:
    for i in range(len(n)):
      n[i][0] = 0


#This is O(n^2) time solution but constant memory. If I had to 
#frequently zero out columns, I would store rows and columns
#twice in a key value store. Same runtime big O but half the 
#actual time
