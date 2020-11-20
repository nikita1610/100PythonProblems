def count_smaller(l):
    n=len(l)
    s=sorted(l)
    a=[]
    for item in l:
        a.append(s.index(item))
    return a
l=[8,1,2,2,3]
ans=count_smaller(l)
print(ans)
