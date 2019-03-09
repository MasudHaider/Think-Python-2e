def check_fermat(a, b, c, n):
    valid = range(3, 100)
    if n in valid:
        if a ** n + b ** n == c ** n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")


prompt = "Enter value for a: "
a = int(input(prompt))
prompt = "Enter value for b: "
b = int(input(prompt))
prompt = "Enter value for c: "
c = int(input(prompt))
prompt = "Enter value for n: "
n = int(input(prompt))

check_fermat(a, b, c, n)
