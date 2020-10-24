import math
def check_perfect(s):
  sum=0
  for i in range(len(s)):
    sum=sum+ord(s[i])
  sq=math.sqrt(sum)
  if sq-math.floor(sq)==0:
    return "YES"
  else:
    return "NO"

s="abcd"
ans=check_perfect(s)
print(ans)
  
    
