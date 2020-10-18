def maximum_sum(mat,n,m):
    sum = -63
    for x in range(0, (n-2)):
        for y in range(0, (m-2)):
            k = sum_hg(mat,x, y)
            if k > sum:
                sum = k
    return sum

def sum_hg(arr ,x, y):
    sum = arr[x][y] + arr[x][y+1] +arr[x][y+2]
    sum = sum + arr[x+1][y+1]
    sum = sum + arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2]
    return sum




mat=    [[0, 3, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [1, 1, 1, 0, 0],
         [0, 0, 2, 4, 4],
         [0, 0, 0, 2, 4]]


n=len(mat)
m=len(mat[0])
s=maximum_sum(mat,n,m)
print(s)
    
