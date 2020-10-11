def majority_element(x,n):
        l=[0]*(max(x)+1)
        for i in range(n):
                l[x[i]]=l[x[i]]+1
        m=max(l)
        if m > n/2:
                return l.index(max(l))
        return -1

x=[3,1,3,3,2]
n=len(x)
ans=majority_element(x,n)
print(ans)
