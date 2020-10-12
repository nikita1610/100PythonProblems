def leaders(x,n):
        *l,last= x
        l1=[]
        l1.append(last)
        for j in reversed(l):
                if j>=last:
                        l1.append(j)
                        last=j
        l1.reverse()
        return l1

x=[16 ,17, 4, 3 ,5, 2]
n=len(x)
l=leaders(x,n)
print(*l)

