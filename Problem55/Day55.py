def reverse_bitonic(s):
  n=len(s)
  i=0
  j=0
  for i in range(1,n):
    if s[i-1]>s[i]:
      continue
    elif s[i-1]<=s[i]:
      break
  if i==n-1:
    return "YES"
  for j in range(i+1,n):
    if s[j]>s[j-1]:
      continue
    elif s[j]<=s[j-1]:
      break
  if j==n-1:
    return "Yes"
  return "NO"


s="zyxbcd"
print(reverse_bitonic(s))
