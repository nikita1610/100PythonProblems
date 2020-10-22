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
    return 1
  for j in range(i+1,n):
    if s[j]>s[j-1]:
      continue
    elif s[j]<=s[j-1]:
      break
  if j==n-1:
    return 1
  return 0

def check_bitonic(mat,n,m):
  for i in range(n):
    if not reverse_bitonic(mat[i]):
      return "NO"
  for i in range(n):
    temp=[0]*n
    for j in range(m):
      temp[j]=mat[j][i]
    if not reverse_bitonic(temp):
      return "NO"
  return "YES"
      
mat=[[2, 3, 4], [1, 2, 3], [4, 5, 6] ]
n=len(mat)
m=len(mat[0])
print(check_bitonic(mat,n,m))
