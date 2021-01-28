def findNth(N):
        a = 0
        i = 0
        while N:
            a += ((10**i)*(N%9))
            N = N//9
            i+=1
        return a
        
N=10
ans=findNth(N)
print(ans)

