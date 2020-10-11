#method 1
def rotate_array(x,d):
        n=len(x)
        reverse(x,0,n-1)
        reverse(x,0,d-1)
        reverse(x,d,n-1)
        

def reverse(x,start,end):
        while(start<end):
                x[start],x[end]=x[end],x[start]
                start+=1
                end-=1



y=[1,2,3,4,5,6,7]
d=2
rotate_array(y,d)
print(y)
