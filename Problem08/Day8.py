#code
def pair(a,left,right,k):
    while(left<right):
        s=a[left]+a[right]
        if s==k:
            return 1
        elif s>k:
            right-=1
        else:
            left+=1
    return 0
    
def triplet(a,s1):
    n=len(a)
    for i in range(n):
        if pair(a,i+1,n-1,s1-a[i]):
            return 1
    return 0


a=[1, 4, 45 ,6, 10, 8]
k=13
a.sort()
print(triplet(a,k))
    
