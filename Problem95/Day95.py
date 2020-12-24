def count_elements(l):
    res = [] 
    for idx in range(0, len(l) - 1):  
        if l[idx] == l[idx + 1]: 
            res.append(l[idx])         
    length = len(list(set(res)))
    return length
    

l = [4, 5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 10]
print(count_elements(l))
  

  

  
