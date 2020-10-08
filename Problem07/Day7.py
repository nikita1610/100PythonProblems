#code
def find_pairs(a,k):
    count=0
    left=0
    right=len(a)-1
    while(left<right):
        s=a[left]+a[right]
        if s==k:
            print(a[left],a[right],k)
            count+=1
            left+=1
            right-=1
        elif s>k:
            right=right-1
        else:
            left=left+1
    if count==0:
        print(-1)

a=[1, 2 ,3, 4 ,5 ,6, 7]
k=8
find_pairs(a,k)
