def is_abecedarian(word):
    alphaord = ord(word[0])
    for i in range(1, len(word)):
        if ord(word[i]) == alphaord:
            continue
        elif ord(word[i]) == alphaord+1:
            alphaord = alphaord+1
            continue
        else:
            return False
    return True


def is_abecedarian_for_loop(word):
    prev = word[0]
    for c in word:
        if c < prev:
            return False
        prev = c
    return True


def is_abecedarian_recursion(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_recursion(word[1:])


if __name__ == '__main__':
    abecedarian = True
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        abecedarian = is_abecedarian_recursion(word)
        if abecedarian:
            print(word)
