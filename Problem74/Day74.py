def power1(x,y):
    ans=1
    for  i in range(1,y+1):
        ans=ans*x
    return ans

def power2(x,y):
    if y==0:
        return 1
    return x*power2(x,y-1)

def power3(x,y):
    if y==0:
        return 1
    elif y%2==0:
        return power3(x,y//2)*power3(x,y//2)
    else:
        return x*power3(x,y//2)*power3(x,y//2)

x=4
y=3
ans1=power1(x,y)
print(ans1)
ans2=power2(x,y)
print(ans2)
ans3=power3(x,y)
print(ans3)
