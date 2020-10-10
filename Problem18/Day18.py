import sys
def find_sum(x):
        sum=0
        max_sum=-sys.maxsize-1
        for i in range(len(x)):
                sum=sum+x[i]
                if sum<0:
                        sum=0
                if sum>max_sum:
                        max_sum=sum

        return max_sum



x=[-2, -3, 4, -1, -2, 1, 5, -3]
ans=find_sum(x)
print(ans)
