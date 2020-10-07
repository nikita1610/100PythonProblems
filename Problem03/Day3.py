#code
def left(a,start,end,x):
    if start>end:
        return -1
    mid=(start+end)//2
    if (a[mid]==x )and (mid==0 or a[mid-1]!=x):
        return mid
    elif a[mid]>=x:
        return left(a,start,mid-1,x)
    else:
        return left(a,mid+1,end,x)

def right(a,start,end,x,n):
    if start>end:
        return -1
    mid=(start+end)//2
    if (a[mid]==x )and (mid==(n-1) or a[mid+1]!=x):
        return mid
    elif a[mid]>x:
        return right(a,start,mid-1,x,n)
    else:
        return right(a,mid+1,end,x,n)
    

a=[1, 3, 5, 5, 5, 5, 67, 123, 125]
n=len(a)
key=5
l=left(a,0, n-1,key)
r=right(a,0,n-1,key,n)
if l==-1 or r==-1:
    print("NOT FOUND")
else:
    print(l,r)
    
    
    
