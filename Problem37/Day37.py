def boolean_matrix(mat,n):
        l=[0]*n*n
        r=[0]*n*n
        for i in range(n):
                for j in range(n):
                        if mat[i][j]==1:
                                l[i]=1
                                r[j]=1
        for i in range(n):
                for j in range(n):
                        if l[i]==1 or r[j]==1:
                                mat[i][j]=1

a=[0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
n=4
mat=[[0 for j in range(n)] for i in range(n)]
k=0
for i in range(n):
    for j in range(n):
        mat[i][j]=a[k]
        k+=1
print(mat)
print("********************")
boolean_matrix(mat,n)
print(mat)
