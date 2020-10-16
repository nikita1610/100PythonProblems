import math
def prime(n):
    if n>1:
        s=int(math.sqrt(n))+1
        flag=0
        for i in range(2,s):
            if n%i==0:
                flag=1
                break
        if flag==0:
            return True
        else:
            return False

def find_sum(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s

a=4
sum2=0
sum1=find_sum(a)
if prime(a):
    print("N0")
else:
    for i in range(2,a):
        while a%i==0:
            sum2=sum2+find_sum(i)
            a=a//i

    if sum1==sum2:
        print("YES")
    else:
        print("NO")
            
