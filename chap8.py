# fruit = 'banana'
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index += 1


# def backward_letter(str):
#     length = len(str)-1
#     while length >= 0:
#         print(str[length])
#         length -= 1
#
#
# def ducklings():
#     prefix = 'JKLMNOPQ'
#     suffix = 'ack'
#
#     for letter in prefix:
#         if letter == 'O' or letter == 'Q':
#             print(letter + 'u' + suffix)
#         else:
#             print(letter + suffix)


# def find(word, letter, index):
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index += 1
#     return -1

# def no_e(string, char, index):
#     counter = 0
#     while index < len(string):
#         if string[index] == char:
#             counter = counter + 1
#         index = index+1
#     print(counter)


# def in_both(w1, w2):
#     for l in w1:
#         if l in w2:
#             print(l)


# word = 'orange'
#
# if word < 'banana':
#     print(word + ' before banana')
# elif word > 'banana':
#     print(word + ' after banana')
# else:
#     print('All right, banana')


def is_reverse(w1, w2):
    if len(w1) != len(w2):
        return False

    i = 0
    j = len(w2)-1

    while not j < 0:
        print(i, j)
        if w1[i] != w2[j]:
            return False
        i = i+1
        j = j-1

    return True


# backward_letter('deepwork')
# ducklings()
# print(find('duckduckgo', 'o', 3))
# no_e('CSrankings', 'Q', 1)
# in_both('apple', 'orange')
print(is_reverse('pots', 'stop'))
