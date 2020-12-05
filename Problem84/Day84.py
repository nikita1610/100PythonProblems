import math
def is_square(s):
    a=int(math.sqrt(s))
    if a*a==s:
        return True
    return False

def check_fibonacci(n):
    s1=5*n*n+4
    s2=5*n*n-4
    if is_square(s1) or is_square(s2):
        return True
    return False

n=8
print(check_fibonacci(n))
