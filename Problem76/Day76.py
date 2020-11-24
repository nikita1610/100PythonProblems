def find_floor(l,start,end,x):
    if start>end:
        return -1
    if x>=l[end]:
        return end
    mid=(start+end)//2
    if l[mid]==x:
        return mid
    if mid>0 and l[mid-1]<=x and x<l[mid]:
        return mid-1
    if x < l[mid]:
        return find_floor(l,start,mid-1,x)
    return find_floor(l,mid+1,end,x)


l=[1,2,4,6,8,10,12,14]
x=7
n=len(l)-1
ans=find_floor(l,0,n,x)
print(l[ans])
