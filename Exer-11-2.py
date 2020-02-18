def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)

    return inverse


if __name__ == "__main__":
    h = histogram("carrot")
    inv = invert_dict(h)
    print(inv)
