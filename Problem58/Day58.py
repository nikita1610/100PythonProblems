def reverse_group(a,n,k):
  for i in range(0,n,k):
    start=i
    end=i+k-1
    if end>n-1:
      end=n-1
    while(start<=end):
      a[start],a[end]=a[end],a[start]
      start+=1
      end-=1
      
  return a

a=[1,2,3,4,5,6,7]
n=len(a)
k=2
ans=reverse_group(a,n,k)
print(*ans)
