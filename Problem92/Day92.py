def product_except(l):
    prod=1
    for item in l:
        prod=prod*item
    a=[]
    for item in l:
        a.append(prod//item)
    return a

l=[1,2,3,4]
a=product_except(l)
print(a)

        
        
