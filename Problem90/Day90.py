def reverse_consonants(s):
    l=[i for i in s]
    n=len(l)
    start=0
    end=n-1
    v=['a','e','i','o','u','A','E','I','O','U']
    while(start<end):
        if l[start] not in v :
            while l[end] in v:
                end-=1
            l[start],l[end]=l[end],l[start]
            start+=1
            end-=1
        else:
            start+=1
    s1="".join(l)
    return s1

s="facade"
ans=reverse_consonants(s)
print(ans)
