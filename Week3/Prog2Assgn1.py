def progression(l):
  if len(l) < 2:
    return(True)
  diff = l[1] - l[0]
  for i in range(2,len(l)):
    if l[i] - l[i-1] != diff:
      return(False)
  return(True)


l1 = [3]
l2 = [7,3,-1,-5]
l3 = [3,5,7,9,10]
print(progression(l1))
print(progression(l2))
print(progression(l3))