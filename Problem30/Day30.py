def transition(a,start,end,k):
        if start>end:
                return -1
        mid=(start+end)//2
        if a[mid]==k and (mid==0 or a[mid-1]!=k):
                return mid
        elif a[mid]>=k:
                return transition(a,start,mid-1,k)
        else:
                return transition(a,mid+1,end,k)


a=[0,0,0,0,1,1]
index=transition(a,0,len(a)-1,1)
print(index)
