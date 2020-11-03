def check_rotated(s1,s2):
  n1=len(s1)
  n2=len(s2)
  if n1!=n2:
    return "NO"
  else:
    temp=s1+s1
    if temp.count(s2)>0:
      return "YES"
    else:
      return "NO"


s1 ="ABCD"
s2 ="CDAB"
ans=check_rotated(s1,s2)
print(ans)
