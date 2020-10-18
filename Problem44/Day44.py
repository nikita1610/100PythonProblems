def remove_duplicates(s):
    l=[0]*26
    ans=""
    for i in range(len(s)):
        ch=ord(s[i])-ord('a')
        if l[ch]==0:
            ans=ans+s[i]
            l[ch]=1
    return ans
                        
s="ababacd"
a=remove_duplicates(s)
print(a)
            
