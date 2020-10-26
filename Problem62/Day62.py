def buy_sell(s):
  l=[]
  flag=0
  i=0
  s.append(-99)
  while(s[i]!=-99):
    if s[i]<s[i+1] and flag==0:
      start=i
      l.append(start)
      flag=1
    elif s[i]>s[i+1] and flag==1:
      end=i
      l.append(i)
      flag=0
    i+=1
  if len(l)==0:
    print("NO PROFIT")
  else:
    for i in range(0,len(l),2):
      print("({} {})".format(l[i],l[i+1]),end=" ")

stocks=[100, 180, 260, 310, 40 ,535, 695]
buy_sell(stocks)
    
