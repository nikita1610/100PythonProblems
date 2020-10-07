def find_set(a):
    a1=list(set(a)) # to avoid duplicates
    a2=[]
    for item in a1:
        a2.append(''.join(sorted(item)))

    ans=[]
    print(a2)
    for word in set(a2):
        indexes=[i for i,x in enumerate(a2) if x==word]
        temp=[]
        for index in indexes:
            temp.append(a1[index])
        ans.append(set(temp))
    return ans

words=['cat', 'dog', 'god', 'cat','tac']
print(find_set(words))
        
        
