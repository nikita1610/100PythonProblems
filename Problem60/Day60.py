a=[1,2,9,15]
n=len(a)
k=n//2
b=0
for i in range(n//2):
  print(a[b],end=' ')
  print(a[k],end=' ')
  b+=1
  k+=1
  if n % 2 ==1:
    print(a[-1],end=' ')
    
    
