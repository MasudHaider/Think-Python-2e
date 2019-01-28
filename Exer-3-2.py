def do_twice(func_arg, value):
    func_arg(value)
    func_arg(value)


def print_spam(value_arg):
    print(value_arg)


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(func_obj, value):
    do_twice(func_obj, value)
    do_twice(func_obj, value)


# do_twice(print_spam, 12)
# do_twice(print_beams, 'spam')
do_four(print_spam, 'cat')
