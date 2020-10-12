def peak_element(x,n):
        if x[0]>x[1]:
                print(x[0],end=" ")
        if x[n-1]>x[n-2]:
                print(x[n-1],end=" ")
        for i in range(1,n-1):
                if x[i]>x[i-1] and x[i]>x[i+1] :
                        print(x[i],end=" ")

x=[10, 20, 15, 2, 23, 90, 67]
n=len(x)
peak_element(x,n)

