import math


def factorial(n):
    if not isinstance(n, int):
        print("Factorial is only defined for integers")
        return None
    elif n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def denominator(kil):
    lower_term = (factorial(kil)**4) * 396**(4*kil)
    return lower_term


def numerator(kiu):
    upper_term = factorial(4*kiu) * (1103 + 26390 * kiu)
    return upper_term


def estimate_pi():
    total_sum = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        dubl = numerator(k) / denominator(k)
        term = factor * dubl
        total_sum += term
        if abs(term) < 1e-15:
            break
        k += 1

    return 1/total_sum


print(estimate_pi())
