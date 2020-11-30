def max_length_subarray(a,b):
    count=0
    ans=0
    for item in a:
        if item in a and item in b:
            count+=1
        else:
            ans=max(count,ans)
            count=0
    return ans


a=[3,6,1,0]
b=[3,6,5,4]
ans=max_length_subarray(a,b)
print(ans)
