def digit_sum(s):
  temp="0"
  n=len(s)
  sum=0
  for i in range(n):
    if (s[i].isdigit()):
      temp=temp+s[i]
    else:
      sum=sum+int(temp)
      temp="0"
  sum=sum+int(temp)
  return sum
      

s="1abc2x30yz67"
print(digit_sum(s))
    
