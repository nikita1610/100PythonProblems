def find_largest(l):
    n=len(l)
    a=sorted(l)
    largest=a[n-1]
    second_largest=a[n-2]
    if 2*second_largest>=largest:
        return l.index(largest)
    else:
        return -1

l=[3,6,1,0]
ans=find_largest(l)
print(ans)
