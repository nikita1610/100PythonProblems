def left(a,start,end,n,k):
        if start > end:
                return -1
        mid=(start+end)//2
        if a[mid]==k and (mid==0 or a[mid-1]!=k):
                return mid
        elif a[mid]>=k:
                return left(a,start,mid-1,n,k)
        else:
                return left(a,mid+1,end,n,k)
        

def right(a,start,end,n,k):
        mid=(start+end)//2
        if start>end:
                return -1
        if a[mid]==k and (mid==n-1 or a[mid+1]!=k):
                return mid
        elif a[mid]>k:
                return right(a,start,mid-1,n,k)
        else:
                return right(a,mid+1,end,n,k)



x=[1, 1, 2, 2, 2, 2, 3]
n=len(x)
k=3
start=0
end=n-1
l=left(x,start,end,n,k)
r=right(x,start,end,n,k)
count=r-l+1
print(count)

