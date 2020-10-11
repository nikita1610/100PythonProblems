x=[4,8,0,9,11,6,5]

k=22
start=0
s1=0
flag=0
for i in range(len(x)):
        s1=s1+x[i]
        while(s1 >k):
                s1=s1-x[start]
                start+=1
        if s1==k:
                print("Found")
                print("Starting Index: ", start)
                print("Ending Index: ",i)
                flag=1

if flag==0:
        print("Subarray Not Found")


