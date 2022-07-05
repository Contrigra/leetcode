def find_occurency(num, arr) -> int:
    occurency = 0
    for i in arr:
        if num == i:
            occurency += 1
    return occurency


def find_it(seq) -> int:
    unique_seq = set(seq)

    for i in unique_seq:
        if find_occurency(i, seq) % 2 != 0:
            return i


def find_it_with_count(seq) -> int:
    unique_seq = set(seq)

    for i in unique_seq:
        if seq.count(i) % 2 != 0:
            return i


print(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5)
print(find_it_with_count([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5)
