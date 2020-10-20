def set_bits(n):
  res=0
  while n>0:
    n = n & (n-1)
    res=res+1
  return res



n=6
print(set_bits(n))
