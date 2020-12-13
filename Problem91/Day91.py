import math
def k_closest(l,k):
    a=[]
    b=[]
    for item in l:
        d=math.sqrt(pow(item[0],2)+pow(item[1],2))
        a.append(d)
    for i in range(k):
        m=a.index(min(a))
        b.append(l[m])
        a.remove(min(a))
    return b

l=[[1,3],[-2,2]]
k=1
print(k_closest(l,k))

        
        
