def smallestpositive(array, n): 
        array.sort()
        ans=1
        for item in array:
            if item <= ans:
                ans+=item
            else:
                break
        return ans
        
array=[1, 10, 3, 11, 6, 15]
ans = smallestpositive(array,len(array))
print(ans)

