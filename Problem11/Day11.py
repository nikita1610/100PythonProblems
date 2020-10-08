#code
def rotate(mat,n):
    for i in range(n):
        for j in range(i,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    
    for i in range(n):
        j=0
        k=n-1
        while j<k:
            temp=mat[j][i]
            mat[j][i]=mat[k][i]
            mat[k][i]=temp
            j+=1
            k-=1
    
    
n=3
a=[1,2,3,4,5,6,7,8,9]
mat=[[0 for j in range(n)] for i in range(n)]
k=0
for i in range(n):
    for j in range(n):
        mat[i][j]=a[k]
        k+=1
rotate(mat,n)
for i in range(n):
    for j in range(n):
        print(mat[i][j],end=" ")
print()
