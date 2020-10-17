import math
def remove_prime(a):
    n=len(a)
    i=0
    while i<n:
        if prime(a[i]):
            a.remove(a[i])
            n=n-1
        else:
            i+=1
    return a


def prime(x):
    if x>1:
        s=int(math.sqrt(x))+1
        flag=0
        for i in range(2,s):
            if x%i==0:
                flag=1
                break
        if flag==1:
            return False
        else:
            return True
    else:
        return False


a=[4, 6, 5, 3, 8, 7, 10, 11, 14, 15]
ans=remove_prime(a)
print(*ans)
            
