import math
def prime(n):
        if n>1:
                s=int(math.sqrt(n))+1
                flag=0
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

n=1
m=10
for i in range(n,m+1):
        if prime(i):
                print(i,end=" ")
                
