def nested_sum(sequence):
    total_sum = 0
    for i in range(0, len(sequence)):
        total_sum += sum(sequence[i])
    return total_sum


t = [[1, 2], [3], [4, 5, 6, 8, 23, 34]]
print(nested_sum(t))
