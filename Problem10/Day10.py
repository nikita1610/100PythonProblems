import math

def prime(n):
    s=int(math.sqrt(n))+1
    flag=0
    if n>1:
        for i in range(2,s):
            if n%i==0:
                flag=1
                break
        if flag==0:
            return True
    else:
        return False


def find_pair(n):
    for i in range(n):
        if prime(i):
            left=n-i
            if prime(left):
                print(i,left)


n=74
find_pair(74)
            
