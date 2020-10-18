def find_next(num,n):
    for i in range(n):
        if num[i]>num[i-1]:
            break
    if i == 1 and num[i] <= num[i-1]: 
         return "Next number not possible"
    x=num[i-1]
    y=i
    for j in range(i+1,n):
        if num[j]>x and num[j]<num[y]:
            y=j
    num[y],num[i-1]=num[i-1],num[y]
    ans=""
    for z in range(i):
        ans=ans+str(num[z])
    s=sorted(num[i:])
    for z in range(len(s)):
        ans=ans+str(s[z])
    return ans
    


n="218765"
l=[int(i) for i in n]
n=len(l)
ans=find_next(l,n)
print(ans)
    
