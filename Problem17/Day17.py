def swap(x):
        start=0
        end=len(x)-1
        while(start<=end):
                if x[start]>=0:
                        x[start],x[end]=x[end],x[start]
                        end=end-1
                else:
                        start=start+1



x=[-4,8,0,-9,-11,6,5]
swap(x)
print(*x)
