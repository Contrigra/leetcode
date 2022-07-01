def two_sum(numbers, target) -> list[int, int]:

    for i in range(len(numbers) - 1):
        for i2 in range(len(numbers)):
            if i == i2:
                continue
            elif numbers[i] + numbers[i2] == target:
                return [i, i2]
    raise Exception


print(two_sum([1234, 5678, 9012], 14690))
print(two_sum([2, 2, 3], 4))
print(two_sum([1,2,3], 4))
