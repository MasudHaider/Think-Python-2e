# def print_spam():
#     print("spam")
#
#
# def do_n(func_obj, n):
#     for i in range(n):
#         func_obj()
#
#
# do_n(print_spam, 4)
import math
signal_power = 9
noise_power = 10
ratio = signal_power // noise_power
decibels = 10 * math.log10(ratio)
print(decibels)