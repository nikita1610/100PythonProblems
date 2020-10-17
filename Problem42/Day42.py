def print_factors(n):
    l=[]
    while n!=1:
        for i in range(2,n+1):
            if n%i==0:
                l.append(i)
                n=int(n/i)
                break
    s=list(set(l))
    s.sort()
    print("Factor---------Power")
    for item in s:
           print(str(item) +"              "+ str(l.count(item)))
           

n=100
print_factors(n)
            
