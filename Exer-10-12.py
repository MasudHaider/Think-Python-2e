def make_word_list():
    wordlist = []
    fin = open('words.txt', 'r')
    for line in fin:
        word = line.strip()
        wordlist.append(word)
    return sorted(wordlist)


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

def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds)


def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True


if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])
