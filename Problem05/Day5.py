def sort_frequency(s):
    d={}
    ans=""
    for item in s:
        if item in d.keys():
            d[item]+=1
        else:
            d[item]=1
    s1=sorted(d.items(),key=lambda item: (item[1], item[0]))
    sorted_keys = [ item[0] for item in s1 ]
    for item in sorted_keys:
            ans+=item*d[item]
        
    return ans

s="stations"
print(sort_frequency(s))
    
