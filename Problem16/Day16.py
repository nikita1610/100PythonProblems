def print_boundary_sum(mat,r,c):
    sum=0
    for i in range(r):
        for j in range(c):
            if i==0 or j==0 or i==r-1  or j==c-1:
                sum+=mat[i][j]
    print(sum)
                
        
mat=    [[1,2,3,4],
	 [5,6,7,8],
	 [1,2,3,4],
	 [5,6,7,8]]
rows=len(mat)
columns=len(mat[0])
print(rows,columns)
print_boundary_sum(mat,rows,columns)


