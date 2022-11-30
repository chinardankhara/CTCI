#constant time solution. just copy next node into current and 
#delete next

#same reference code as 2_1
def delete_middle_node(n):
  n.set_data(n.get_next().get_data())
  n.set_next(n.get_next().get_next())