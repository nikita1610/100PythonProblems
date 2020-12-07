def length_longest(l):
    n=len(l)
    ans=1
    count=1
    for i in range(0,n-1):
        if l[i]<l[i+1]:
            count+=1
            ans=max(count,ans)
        else:
            count=1
    return ans

l=[1,2,5,4,7]
ans=length_longest(l)
print(ans)
