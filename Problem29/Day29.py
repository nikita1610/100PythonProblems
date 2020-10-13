def find_row(mat,n,m):
        max1=0
        index=-1
        for i in range(n):
                count=mat[i].count(1)
                if count>max1:
                        max1=count
                        index=i
        return index


mat = [[0 ,1 ,1 ,1],
       [0, 0,1 ,1],
       [0 ,0, 1, 1]]
n=len(mat)
m=len(mat[0])
row=find_row(mat,n,m)
print(row)
