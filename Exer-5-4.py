def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


recurse(3, 0)
print("__main__")
print("recurse n --> 3, s --> 0")
print("recurse n --> 2, s --> 3")
print("recurse n --> 1, s --> 5")
print("recurse n --> 0, s --> 6")
