def find_row(mat,n,a):
        l=[]
        for i in range(n):
                count=mat[i].count(1)
                if count>0:
                    l.append(count)
                else:
                    l.append(n)
        if sum(a)==0:
            return -1
        else:
            m=min(l)
            return l.index(m)

a=[0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
n=4
mat=[[0 for j in range(n)] for i in range(n)]
k=0
for i in range(n):
    for j in range(n):
        mat[i][j]=a[k]
        k+=1

row=find_row(mat,n,a)
print(row)
