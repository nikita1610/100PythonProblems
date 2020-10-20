def power_set(s):
  n=len(s)
  size=1<<n
  l=[]
  for i in range(size):
    ans=""
    for j in range(n):
      if (i & 1<<j)>0:
        ans=ans+s[j]
    l.append(ans)
  l.sort()
  return l

s="abc"
print(power_set(s))
