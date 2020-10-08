def iterative_hailstone(n):
    ans=[]
    while n>1:
        ans.append(n)
        if n%2==1:
            n=(3*n)+1
        else:
            n=n//2
    ans.append(1)
    return ans

def recursive_hailstone(n,ans=[]):
    if n==1:
        ans.append(n)
        return ans
    ans.append(n)
    if n%2==1:
        return recursive_hailstone( n*3+1,ans)
    else:
        return recursive_hailstone(n//2,ans)

n=17
a=iterative_hailstone(n)
print(a)
s=17
a1=recursive_hailstone(s)
print(a1)



            
