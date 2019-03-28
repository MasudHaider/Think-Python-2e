import math


def mysqrt(a):
    epsilon = 0.0000001
    x = a - 1
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return y


def test_square_root(a):
    sr_math = math.sqrt(a)
    sr_mysqrt = mysqrt(a)
    diff = abs(sr_math - sr_mysqrt)


if __name__ == '__main__':
    a = 1
    while a < 10:
        test_square_root(a)
        a = a+1
