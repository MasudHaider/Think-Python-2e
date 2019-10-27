def is_sorted(seq):
    for i in range(0, len(seq)-1):
        if seq[i] < seq[i+1]:
            continue
        return False

    return True


if __name__ == '__main__':
    lists = [1, 2, 5, 3, 4]
    strlist = ['b', 'v', 'a', 'c']
    print(is_sorted(lists))
    print(is_sorted(strlist))
