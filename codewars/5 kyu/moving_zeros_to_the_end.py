def move_zeros(arr):
    zeros = arr.count(0)

    for _ in range(zeros):
        arr.remove(0)
        arr.append(0)

    return arr



arr = [9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]
result_arr = [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

arr = move_zeros(arr)
print(arr)
print(arr == result_arr)
