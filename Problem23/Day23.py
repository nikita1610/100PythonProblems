arr=[1,2,2,3,4,1]
count = 0
n=len(arr)
for i in range(n):
        Sum = arr[i]
        if Sum % 2 == 0:
            count += 1
        for j in range(i+1,n):
            Sum += arr[j]
            if Sum%2 == 0:
                count += 1
print(count)
