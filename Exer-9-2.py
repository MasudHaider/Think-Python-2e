def has_no_e(word_param):
    if 'e' in word_param:
        return False
    return True


if __name__ == '__main__':
    fin = open('words.txt')
    has_e_bool = True
    words = 0
    no_e = 0
    for line in fin:
        word = line.strip()
        words += 1
        has_e_bool = has_no_e(word)
        if has_e_bool:
            no_e += 1
            print(word)
    print((no_e / words) * 100)
