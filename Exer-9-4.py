def uses_only(words, list):
    for letter in words:
        if letter in list:
            continue
        else:
            return False
    return True


def make_sentence(req_letters):
    for l in range(0, len(req_letters)):
        print(req_letters[l] + req_letters[-l], end=" ")


if __name__ == '__main__':

    has_required_letter = True
    required_letters = input("Enter required letter: ")
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        has_required_letter = uses_only("qwerty", required_letters)
        if has_required_letter:
            print(has_required_letter)

    make_sentence("acefhlo")




