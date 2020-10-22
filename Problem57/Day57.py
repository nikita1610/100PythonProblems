def min_to_balance(a,n):
  left_sum=0
  right_sum=0
  mid=(n//2)
  for i in range(mid):
    left_sum=left_sum+a[i]
    right_sum=right_sum+a[n-i-1]
  ans=abs(left_sum-right_sum)
  return ans

a=[1, 5, 3, 2]
n=len(a)
print(min_to_balance(a,n))
