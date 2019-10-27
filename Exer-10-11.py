def reverse_list_words(sequence):
    reversed_list = [character[::-1] for character in sequence]
    return reversed_list


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
    counter = 0
    words = make_word_list()
    reversed_words = reverse_list_words(words)
    for i in range(0, len(words)):
        if in_bisect(words, reversed_words[i]):
            # counter += 1
            print(words[i], reversed_words[i])
    # print(counter) = 885
