def swap(a,n):
    i=0
    j=1
    while(i<n and j<n):
        while(i<n and a[i]%2 == 0):
            i+=2
        while(j<n and a[j]%2 == 1):
            j+=2
        if i< n and j<n:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp


a=[4,2,5,7]
n=len(a)
swap(a,n)
print(*a)
