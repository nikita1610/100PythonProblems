def alternate(x):
    l=[]
    n=len(x)
    x.sort()
    mid=int(n/2)
    for i in range(0,mid+1):
        if i==mid:
            l.append(x[n-i-1])
        else:
            l.append(x[n-i-1])
            l.append(x[i])

    return l


x=[7,1,2,3,4,5,6]
ans=alternate(x)
print(*ans)
    
                                
                
