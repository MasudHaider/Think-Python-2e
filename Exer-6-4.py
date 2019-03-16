def is_power(a, b):
    if a == b:
        return True
    if b == 0 or b == 1:
        return False
    c = int(a/b)
    if a % b == 0 and is_power(c, b):
        return True


print(is_power(1000, 10))
