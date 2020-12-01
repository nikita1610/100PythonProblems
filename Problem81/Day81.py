def check_self_divide(n):
    flag=0
    s1=str(n)
    for item in s1:
        item=int(item)
        if n%item!=0:
            flag=1
            break
    if flag==1:
        return False
    else:
        return True
n=128
print(check_self_divide(n))
