def wave_sort(a,n):
  for i in range(0,n,2):
    if i>0 and a[i-1]>a[i]:
      a[i],a[i-1]=a[i-1],a[i]

    if i<n-1 and a[i+1]>a[i]:
      a[i+1],a[i]=a[i],a[i+1]

  return a

l=[10, 5, 6, 3, 2, 20, 100, 80]
n=len(l)
ans=wave_sort(l,n)
print(*ans)
