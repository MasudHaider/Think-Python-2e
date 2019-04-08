fruit = 'noon'
print(fruit[::-1])


def is_palindrome(word):
    if word[:] == word[::-1]:
        return True


print(is_palindrome('noon'))
print(is_palindrome('redivider'))
