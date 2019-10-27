def chop(seq):
    del seq[::len(seq)-1]
    return None


lists = [1, 2, 3, 4]
chop(lists)
print(lists)
