def ack(m, n):
    if m < 0 or n < 0:
        print("Ackermann is not defined for negative integers")
    elif m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))


print(ack(3, 4))
