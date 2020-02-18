def has_duplicates(t):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = ['sleep', 'bone', 'dog']
    print(has_duplicates(t))
    t.append('bone')
    print(has_duplicates(t))

    t = ['jelly', 'kite', 'cat']
    print(has_duplicates2(t))
    t.append('cat')
    print(has_duplicates2(t))
