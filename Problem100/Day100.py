def ValidPair(a, n): 
    	a.sort()
    	p=0
    	q=n-1
    	ans=0
    	while(p<=q):
    	    if a[p]+a[q]<=0:
    	        p+=1
    	    else:
    	        ans+=q-p
    	        q-=1
    	        #ans+=1
    	return ans
    
a=[3,-1,2]
ans=ValidPair(a,len(a))
print(ans)
