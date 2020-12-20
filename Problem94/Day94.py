from string import punctuation

  
def get_pnc_count(strng): 
    return len([ele for ele in strng if ele in punctuation])

def get_list(l):
    l.sort(key = get_pnc_count)
    return l
  
l = ["Hello@%^", "Best!"]
a=get_list(l)
print(a)

        
        
