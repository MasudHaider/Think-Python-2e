def any_islower1(s):  # checks whether the first character of the string is lowercase or not
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_islower2(s):
    for c in s:
        if 'c'.islower():   # returns string 'True/False' for 'c', doesn't check string parameter
            return 'True'
        else:
            return 'False'


def any_islower3(s):
    for c in s:
        flag = c.islower()             # checks every character of string for lowercase, but
    return flag                        # returns the result only for the last character


def any_islower4(s):          # returns True if there is one or more lowercase letters, otherwise false
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_islower5(s):   # returns true if all characters are lowercase, otherwise false
    for c in s:
        if not c.islower():
            return False
    return True


print(any_islower4('NETHErLAND'))
