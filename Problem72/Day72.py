def count_subarray01(l,n):
  d={}
  ans=0
  s=0
  d[0]=1
  for i in range(n):
    if l[i]==0:
      l[i]=-1
    s=s+l[i]
    if s in d.keys():
      d[s]+=1
    else:
      d[s]=1
  for key in d.keys():
    ans=ans+ ((d[key])*(d[key]-1))//2
  return ans

n=7
l=[1, 0, 0, 1, 0, 1, 1]
print(count_subarray01(l,n))
