def odd(x,n):
  res=0
  z=0
  y=0
  for item in x:
    res=res^item
  set_bit= res &~(res-1)
  for item in x:
    if item & set_bit:
      z=z^item
    else:
      y=y^item
  return (z,y)

x=[4, 2, 4, 5, 2, 3, 3, 1]
n=len(x)
print(odd(x,n))
