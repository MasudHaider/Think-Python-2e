def check_fermat(a, b, c, n):
    valid = range(3, 100)
    if n in valid:
        if a ** n + b ** n == c ** n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")


check_fermat(3, 5, 4, 5)
