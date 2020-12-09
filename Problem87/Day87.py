def moves(a):
    m=max(a)
    s=0
    for item in a:
        s=s+abs(m-item)
    return s

a=[1,2,3]
ans=moves(a)
print(ans)
