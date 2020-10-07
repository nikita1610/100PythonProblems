# Approach 1 using separate lists for storing the sum from both right and left
# Space Complexity : n
# Time Complexity : O(n)
def find_index1(a):
    sum_left=[]
    sum_right=[]
    sum=0
    ans=-1
    for item in a:
        sum+=item
        sum_left.append(sum)

    for item in a:
        sum_right.append(sum)
        sum-=item

    for i in range(len(sum_left)):
        if sum_left[i]==sum_right[i]:
            ans=i
    
        
    return ans

# traversing the list from both ends and finding the element
def find_index2(a):
    ans=-1
    left=0
    right=len(a)-1
    left_sum=a[left]
    right_sum=a[right]
    while(left<=right):
        if left_sum==right_sum and left+2==right:
            ans=left+1
            return ans
        elif left_sum > right_sum :
            right=right-1
            right_sum=right_sum+a[right]
        else:
            left=left+1
            left_sum=left_sum+a[left]
    return ans

a=[4,2,5,1,2,3]
a1=find_index1(a)
print(f"The matching index from approach 1 is {a1}")
a2=find_index2(a)
print(f"The matching index from approach 2 is {a2}")

            
    
        
