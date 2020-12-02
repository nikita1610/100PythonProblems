def winner(votes):
    d={}
    for item in votes:
        if item in d.keys():
            d[item]+=1
        else:
            d[item]=1
    #print(d)
    a=sorted(d.items(),key=lambda k:(-k[1],k[0]))
    return a[0][0]
votes= ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john","johnny", "jamie", "johnny", "john"]
ans=winner(votes)
print(ans)