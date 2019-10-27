def has_duplicates(sequence):
    strings = (''.join(str(x) for x in sequence))
    for l in strings:
        if strings.count(l) > 1:
            return True
        continue

    return False


if __name__ == '__main__':
    lists = ['s', 'i', 'l', 'e', 'n', 't']
    print(has_duplicates(lists))
    print(lists)
