def fizzbuzz(target) -> list:
    arr = []
    for i in range(1, target + 1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append('FizzBuzz')
        elif i % 3 == 0:
            arr.append('Fizz')
        elif i % 5 == 0:
            arr.append('Buzz')
        else:
            arr.append(i)

    return arr


expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
assert fizzbuzz(10) == expected
