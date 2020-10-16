def lcs(a):
        a.sort()
        c=1
        m=1
        for i in range(1,len(a)):
                if a[i]-a[i-1]==1:
                        c+=1
                        m=max(c,m)
                else:
                        c=1
        return m
                

a=[2, 6, 1 ,9 ,4, 5 ,3]
ans=lcs(a)
print(ans)

