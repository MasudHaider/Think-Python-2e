def cumsum(seq):
    new_list = []
    for i in range(0, len(seq)):
        new_list.append(sum(seq[0:i+1]))
    return new_list


if __name__ == '__main__':
    my_list = [1, 2, 3, 67]
    print(cumsum(my_list))
