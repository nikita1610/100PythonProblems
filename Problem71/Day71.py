def reverse_string(s):
  s1=list(s)
  n=len(s)
  i=0
  j=n-1
  while i<j:
    if not s1[i].isalpha():
      i+=1
    elif not s1[j].isalpha():
      j-=1
    else:
      s1[i],s1[j]=s1[j],s1[i]
      i+=1
      j-=1
  return "".join(s1)
    

s="abc/defgh$ij"
print(reverse_string(s))
