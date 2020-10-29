def check_anagram(s1,s2):
  n1=len(s1)
  n2=len(s2)
  if n1!=n2:
    return "NO"
  else:
    flag=0
    l=[0]*26
    for i in range(n1):
      l[ord(s1[i])-ord('a')]+=1
      l[ord(s2[i])-ord('a')]-=1
    for j in range(26):
      if l[j]!=0:
        flag=1
        break
    if flag==0:
      return "YES"
    else:
      return "NO"
        
s1="allergy" 
s2="allergic"
ans=check_anagram(s1,s2)
print(ans)

