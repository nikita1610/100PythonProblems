def find_left_non_repeating1(s):
  n=len(s)
  l=[0]*256
  index=-1
  for i in range(n):
    l[ord(s[i])]+=1
  for i in range(n):
    if l[ord(s[i])]==1:
      index=i
      char=s[i]
      break
  if index==-1:
    return "NOT FOUND"
  else:
    return (index,char)

def find_left_non_repeating2(s):
  visited=[False]*256
  n=len(s)
  res=-1
  for i in range(n-1,-1,-1):
    if (visited[ord(s[i])]):
      continue
    else:
      visited[ord(s[i])]=True
      res=i
      char=s[i]
  return (res,char)

s="abcdabce"
index=find_left_non_repeating1(s)
print(index)

index2=find_left_non_repeating2(s)
print(index2)
