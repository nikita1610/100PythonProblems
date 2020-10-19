def trap_water(x,n):
  left=[0]*n
  right=[0]*n
  ans=0
  left[0]=x[0]
  for i in range(1,n):
    left[i]=max(left[i-1],x[i])
  right[n-1]=x[n-1]
  for i in range(n-2,-1,-1):
    right[i]=max(right[i+1],x[i])
  for i in range(0,n):
    ans+=min(left[i],right[i])-x[i]
  return ans



x=[7,4,0,9]
n=len(x)
ans=trap_water(x,n)
print(ans)
    
