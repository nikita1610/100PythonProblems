import math
def prime(n):
    flag=0
    if n>1:
        s=int(math.sqrt(n))+1
        for i in range(2,s):
            if n%i==0:
                flag=1
                break
        if flag==1:
            return False
        else:
            return True
    else:
        return False


n=30
l=[]
for i in range(n):
    if prime(i):
        ans=str(i)
        if "3" in ans or "7" in ans:
            l.append(int(ans))
print(l)
    
