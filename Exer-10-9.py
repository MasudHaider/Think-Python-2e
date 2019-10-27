import time


def list_from_words():
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)

    return word_list


def list_from_words_idiom():
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list += [word]

    return word_list


if __name__ == '__main__':
    start = time.time()
    append_list = list_from_words()
    print(append_list[:100])
    f1_time = time.time() - start
    print("appending seconds : ", f1_time)
    start = time.time()
    idiom_list = list_from_words_idiom()
    f2_time = time.time() - start
    print(idiom_list[:100])
    print("idiom seconds : ", f2_time)
