def find_sum(n):
    s=0
    while(n):
        s+=n%10
        n=n//10
    return s

n=5601
while(n//10):
    n=find_sum(n)

print(n)
    
                                
                
