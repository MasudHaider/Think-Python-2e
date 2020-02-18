def dict_from_words():
    word_dict = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_dict[word] = word + 'o'
    return word_dict


def histogram(d, s):
    for c in d:
        if d[c] == s:
            return True
    return False


words_dictionary = dict_from_words()
print(histogram(words_dictionary, 'aaho'))
