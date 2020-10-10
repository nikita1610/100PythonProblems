#method 1
def rotate_one(x):
        temp=x[0]
        n=len(x)
        for i in range(0,n-1):
                x[i]=x[i+1]
        x[n-1]=temp

def rotate_array1(x,d):
        for i in range(d):
                rotate_one(x)

#method 2
def rotate_array2(x,d):
        n=len(x)
        reverse(x,0,d-1)
        reverse(x,d,n-1)
        reverse(x,0,n-1)

def reverse(x,start,end):
        while(start<end):
                x[start],x[end]=x[end],x[start]
                start+=1
                end-=1



x=[1,2,3,4,5,6,7]
d=2
rotate_array1(x,d)
print(x)

y=[1,2,3,4,5,6,7]
rotate_array2(y,d)
print(y)
