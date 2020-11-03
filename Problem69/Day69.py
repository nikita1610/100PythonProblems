def reverse(a,start,end):
  while(start<=end):
    a[start],a[end]=a[end],a[start]
    start+=1
    end-=1

def circular_sorted(a):
  n=len(a)
  min_index=0
  minimum=a[0]
  for i in range(1,n):
    if a[i]<minimum:
      minimum=a[i]
      min_index=i
  reverse(a,0,min_index-1)
  reverse(a,min_index,n-1)
  reverse(a,0,n-1)
  return a

a=[3,4,5,1,2]
l=circular_sorted(a)
print(l)

