def call_beams(func, value1, value2):
    do_twice(func, value1, value2)
    print_value('+')


def call_posts(func_obj, val1, val2):
    do_four(func_obj, val1, val2)
    do_four(func_obj, val1, val2)
    do_four(func_obj, val1, val2)
    do_four(func_obj, val1, val2)


def do_twice(func_arg, value1, value2):
    func_arg(value1, value2)
    func_arg(value1, value2)


def do_four(func_obj, value1, value2):
    do_twice(func_obj, value1, value2)
    print_beams(value1, value2)
    print('')


def print_beams(arg1, arg2):
    print(arg1 + (' ' + arg2) * 4, end=' ')


def print_value(value):
    print(value)


call_beams(print_beams, '+', '-')
call_posts(print_beams, '|', ' ')
call_beams(print_beams, '+', '-')
call_posts(print_beams, '|', ' ')
call_beams(print_beams, '+', '-')
