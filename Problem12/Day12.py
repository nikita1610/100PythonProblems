#code
def find(mat,n,x):
    largest=mat[n-1][n-1]
    smallest=mat[0][0]
    l=[]
    if x < smallest and x>largest:
        return "NOT FOUND"
    i=0
    j=n-1
    while(i<n and j>=0):
        if mat[i][j]==x:
            l.append(i)
            l.append(j)
            return l
        elif mat[i][j]>x:
            j-=1
        else:
            i+=1
    return "NOT FOUND"
            
    
    
n=4
a=[10, 20, 30, 40,15, 25, 35, 45,27, 29, 37, 48,32, 33, 39, 50]
mat=[[0 for j in range(n)] for i in range(n)]
k=0
x=29
for i in range(n):
    for j in range(n):
        mat[i][j]=a[k]
        k+=1
ans=find(mat,n,x)
if isinstance(ans,list):
    print(*ans)
else:
    print(ans)
