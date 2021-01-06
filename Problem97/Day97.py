def isHappy(n):
    d=set()
    while n not in d:
        d.add(n)
        t = n
        s = 0  # sum
        while t != 0:
            digit = (t % 10)
            s += digit * digit
            t //= 10
        n = s
        if n == 1:
            return True
    return False

n=19
print(isHappy(n))
