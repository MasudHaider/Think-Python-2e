def avoids(words, forbw):
    for letter in forbw:
        if letter in words:
            return False
    return True


def permutations_with_repetition(permutable):
    base = len(permutable)
    for n in range(base ** base):
        yield "".join(permutable[n // base ** (base - d - 1) % base] for d in range(base))


if __name__ == '__main__':
    for p in permutations_with_repetition("lion"):
        print(p)
    has_no_fl = True
    forbidden_letter = input("Enter forbidden word: ")
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        has_no_fl = avoids(word, forbidden_letter)
        if has_no_fl:
            print(word)




