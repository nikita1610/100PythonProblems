def find_substring(s,k):
    substr_list=[]
    j=len(s)-k+1
    for i in range(j):
        substr_list.append(s[i:i+k])
    return sorted(substr_list)

s="stack"
k=3
s1=find_substring(s,k)
print(f"Smallest substring of size k is {s1[0]}")
print(f"Largest substring of size k is {s1[-1]}")
    
    
    
