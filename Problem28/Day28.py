def prime(n):
        a=[True for i in range(n+2)]
        for i in range(2,n+1):
                if a[i]==True:
                        for j in range(i*i,n+1,i):
                                a[j]=False
        for i in range(2,n+1):
                if a[i]==True:
                        print(i,end=" ")


n=27
prime(27)
