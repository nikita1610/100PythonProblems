def find_missing(x,k):
    i=1
    c=[]
    while k!=0:
        if i not in x:
            c.append(i)
            k-=1
        i+=1
    return c

x=[2,3,4]
k=4
c=find_missing(x,k)
print(*c)
            
