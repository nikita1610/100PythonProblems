def find_ceil(l,start,end,x):
    if start>end:
        return -1
    if x>l[end]:
        return -1
    if x<=l[start]:
        return start
    mid=(start+end)//2
    if l[mid]==x:
        return mid
    elif l[mid]<x:
        if mid+1<=end and x<=l[mid+1]:
            return mid+1
        else:
            return find_ceil(l,mid+1,end,x)
    else:
        if mid-1>=start and x>l[mid-1]:
            return mid-1
        else:
            return find_ceil(l,start,mid-1,x)
    


l=[1,2,4,6,8,10,12,14]
x=7
n=len(l)-1
ans=find_ceil(l,0,n,x)
print(l[ans])
