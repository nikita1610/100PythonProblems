import math
def find_sum(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s


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


n=5601
while(n//10):
    n=find_sum(n)
print("Sum of digits is" , n)
if prime(n):
    print("Prime")
else:
    print("Not Prime")
    
                                
                
