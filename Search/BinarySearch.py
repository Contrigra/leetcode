def binary_search(array, seeked_number):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = array[mid]
        if guess == seeked_number:
            return mid

        if guess > seeked_number:
            high = mid - 1

        if guess < seeked_number:
            low = mid + 1

    return "There's no such number!"


arr = [20, 30, 40, 50, 80, 90, 100]

print(binary_search(arr, 45))
print(binary_search(arr, 40))