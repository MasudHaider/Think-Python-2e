def recurse(n, s):
    """Recursively call the function until base case is met.
    n being 0 will exit the function
    Otherwise call recurse()"""
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


recurse(-1, 0)
