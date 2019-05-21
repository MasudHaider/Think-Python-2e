def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.

    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


if __name__ == '__main__':
    triple_double = True
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        triple_double = is_triple_double(word)
        if triple_double:
            print(word)
