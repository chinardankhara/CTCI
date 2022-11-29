def string_rotation(a, b):
  if a in b + b: return True
  return False

#linear time
#for a string divided into x and y where a = xy and b = yx, 
#xy is always in yxyx, so a always in b + b
