def gcd(a, b):
    if a >= 1 and b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)


print(gcd(24, 6))
