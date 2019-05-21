def uses_all(words, required):
    for letter in required:
        if letter not in words:
            return False
    return True


def uses_vowel(word, vowel):
    counter = 0
    if vowel in word:
        print(word)
        counter = counter + 1
    return counter


if __name__ == '__main__':
    has_required_letter = True
    vowels = 'aeiou'
    vowel_counter = 0
    required_letters = input("Enter required letters: ")
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        has_required_letter = uses_all(word, required_letters)
        if has_required_letter:
            print(word)
        vowel_counter = uses_vowel(word, vowels)
        aeiouy_counter = uses_vowel(word, vowels+'y')
    print("words with vowels: ", vowel_counter, "\nwords with aeiouy: ", aeiouy_counter)







