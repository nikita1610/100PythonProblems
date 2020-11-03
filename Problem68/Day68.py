def image_inversion(mat,n,m):
  for i in range(n):
    start=0
    end=m-1
    while(start<=end):
      mat[i][start],mat[i][end]=mat[i][end],mat[i][start]
      start+=1
      end-=1
  for i in range(n):
    for j in range(m):
      if mat[i][j]==0:
        mat[i][j]=1
      elif mat[i][j]==1:
        mat[i][j]=0
  return mat

mat=[[1,1,0],[1,0,1],[0,0,0]]
n=len(mat)
m=len(mat[0])
ans=image_inversion(mat,n,m)
print(ans)
