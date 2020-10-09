def print_boundary(mat,r,c):
        for j in range(c):
            print(mat[0][j],end=" ")
        for i in range(1,r-1):
            print(mat[i][0],end=" ")
            print(mat[i][c-1],end=" ")
        for x in range(c):
            print(mat[r-1][x],end=" ")
        print()



mat=    [[1,2,3,4],
	 [5,6,7,8],
	 [1,2,3,4],
	 [5,6,7,8]]
rows=len(mat)
columns=len(mat[0])
print(rows,columns)
print_boundary(mat,rows,columns)


