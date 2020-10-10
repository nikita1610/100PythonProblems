def sort01(x):
        start=0
        end=len(x)-1
        while(start<=end):
                if x[start]==1:
                        x[start],x[end]=x[end],x[start]
                        end-=1
                else:
                        start+=1



x=[1,1,0,0,1,1,0,1,0]
sort01(x)
print(*x)
