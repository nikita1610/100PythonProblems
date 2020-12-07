def is_increasing(l):
    n=len(l)
    flag=0
    for i in range(0,n-1):
        if l[i]>l[i+1]:
            flag=1
            break
    if flag==1:
        return False
    else:
        return True

def is_decreasing(l):
    n=len(l)
    flag=0
    for i in range(0,n-1):
        if l[i]<l[i+1]:
            flag=1
            break
    if flag==1:
        return False
    else:
        return True
    
def check_montonic(l):
    if is_increasing(l) or is_decreasing(l):
        return True
    return False

l=[7,5,4,4,3,2]
ans=check_montonic(l)
print(ans)
