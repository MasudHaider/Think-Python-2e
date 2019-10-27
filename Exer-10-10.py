def make_word_list():
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)

    return sorted(word_list)


def in_bisect(seq, value):
    if len(seq) == 0:
        return False
    length = len(seq) // 2
    if seq[length] == value:
        return True
    elif seq[length] > value:
        return in_bisect(seq[:length], value)
    else:
        return in_bisect(seq[length+1:], value)


if __name__ == '__main__':
    sorted_list = make_word_list()
    word_in_list = in_bisect(sorted_list, 'green')
    print(word_in_list)
