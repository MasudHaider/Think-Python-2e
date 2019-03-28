import math


def mysqrt(a_m):
    x = a_m / 5
    while True:
        y = (x + a_m / x) / 2
        if y == x:
            return x
        x = y


def test_square_root(a_test):
    sr_math = math.sqrt(a_test)
    sr_mysqrt = mysqrt(a_test)
    diff = abs(sr_mysqrt - sr_math)

    print('{:<7}''{:<21}''{:<23}'.format(a_test, sr_mysqrt, sr_math), diff)


if __name__ == '__main__':
    a = 1
    print('a', 'mysqrt(a)'.rjust(14), 'math.sqrt(a)'.rjust(23), 'diff'.rjust(15))
    print('-', '---------'.rjust(14), '------------'.rjust(23), '----'.rjust(15))
    while a < 10:
        test_square_root(a)
        a = a+1
