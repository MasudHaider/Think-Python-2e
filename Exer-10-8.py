import random


def generate_age():
    randi = random.randint(1, 100)
    return randi


def count_pairs(n):
    return n*(n-1)/2


def n_different_bday(n):
    return (364/365)**n*(n-1)/2


def different_bday():
    return 364/365


def birthday_match(n):
    match = 1 - (364/365)**(n*(n-1)/2)
    return match


if __name__ == '__main__':
    age = generate_age()
    pairs = count_pairs(age)
    unmatched = n_different_bday(age)
    matches = birthday_match(age)
    print("Matching percentage: "+"{:.2%}".format(matches))
    print("Unmatched percentage: "+"{:.2%}".format(unmatched))
