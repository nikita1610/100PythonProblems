def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)


def check_strong(n):
    s=str(n)
    ans=0
    l=[int(i) for i in s]
    for item in l:
        ans=ans+factorial(item)
    if ans==n:
        return "YES"
    else:
        return "NO"

n=145
print(check_strong(n))
            
