def check_set_bit(n,k):
  if n & (1<<k):
    return "YES"
  else:
    return "NO"


n=4
k=0
print(check_set_bit(n,k))
