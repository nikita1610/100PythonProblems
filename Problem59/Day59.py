def faults(a,n,cap):
  cache=[]
  faults=0
  for i in a:
    if (i not in cache):
      if len(cache)==cap:
        cache.pop(0)
        cache.append(i)
      else:
        cache.append(i)
      faults+=1
    else:
      cache.remove(i)
      cache.append(i)
  print(faults)


n=9
a=[5, 0, 1, 3, 2, 4, 1, 0, 5]
cap=4
faults(a,n,cap)
    
