def equidistant(item):
    flag=0
    for i in range(len(item)-1):
        if (ord(item[i+1])-ord(item[i]))!=(ord(item[1])-ord(item[0])):
            flag=1
            break
    if flag==1:
        return False
    else:
        return True
    
def count_equidistant(l):
    res = [] 
    for item in l:
        if equidistant(item):
            res.append(item)
    
    return res
l = ["abcd", "egil", "mpsv", "abd"] 
print(count_equidistant(l))
  

  

  
