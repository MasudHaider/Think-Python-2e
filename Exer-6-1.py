def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a(p, q):
    p = p + 1
    return p * q


def c(i, j, k):
    total = i + j + k
    square = b(total)**2
    return square


if __name__ == '__main__':
    x = 1
    y = x + 1
    print(c(x, y + 3, x + y))
    
    print("Stack Diagram:")
    print("c(i, y+3, i+y) --> c(1,5,3) --> print(8100)")
    print("square = b(total)**2 --> b(90) ** 2 --> return 8100")
    print("prod = a(i, y) --> a(9,9) --> return 90")
    print("a(i, y) --> a(9,9) --> return 90")
