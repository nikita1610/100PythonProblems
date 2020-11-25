def find_score(s):
    n=len(s)
    l=[i for i in s]
    count1=0
    count0=0
    ans=0
    for i in range(len(l)):
        if l[i]=="1":
            count1+=1
    for i in range(len(l)):
        if l[i]=="1":
            count1-=1
        else:
            count0+=1
        a=count1+count0
        ans=max(a,ans)
    return ans
    


s="011101"
ans=find_score(s)
print(ans)
