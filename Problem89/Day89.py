def check_binary_palindrome(n):
    l=[]
    while(n>0):
        l.append(n%2)
        n=n//2
    b1="".join(map(str,l))
    b2=b1[::-1]
    return b1==b2

n=9
ans=check_binary_palindrome(n)
print(ans)
