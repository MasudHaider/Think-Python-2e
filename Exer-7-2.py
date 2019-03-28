import math


def eval_loop():
    while True:
        ein = input()
        if not ein == 'done':
            eval_result = eval(ein)
            print(eval_result)
        else:
            return eval_result


if __name__ == '__main__':
    print(eval_loop())
