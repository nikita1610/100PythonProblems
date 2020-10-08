def minCost(f):
  
    cost=0
  
    while(len(f)>1):
        min1=min(f)
        f.remove(min1)
  
        min2=min(f)
        f.remove(min2)
  
        f.append(min1+min2)
        cost= cost+min1+min2
  
    return cost

orders= [14, 25, 5, 8 ]
cst=minCost(orders)
print(cst)
