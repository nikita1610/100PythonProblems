def reduced_list(x):
        l=[]
        for item in x:
                l.append(item)
        l.sort()
        for item in x:
                print(l.index(item),end=" ")


x=[20,10,30,50,40]
reduced_list(x)
