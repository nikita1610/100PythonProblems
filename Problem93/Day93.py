def move_zeroes(l):
    start=0
    end=len(l)-1
    while(start<end):
        if l[start]==0:
            l[start],l[end]=l[end],l[start]
            end-=1
        else:
            start+=1
    return l

l=[0,0,1,2,0,3]
a=move_zeroes(l)
print(a)

        
        
