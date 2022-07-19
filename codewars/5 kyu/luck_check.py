def chunkify_even(number):
    arr = []
    middle = len(number) // 2
    arr.append(number[0:middle])
    arr.append(number[middle:])
    return arr

def luck_check(number: str) -> bool:
    number_length = len(number)
    if number_length % 2 != 0:
        number = number[:number_length // 2] + number[number_length // 2 + 1:]

    arr = chunkify_even(number)

    return sum([int(i) for i in arr[0]]) == sum([int(i) for i in arr[1]])


print(luck_check('17935') is True)
print(luck_check('683179') is True)

assert luck_check('683000') is False
