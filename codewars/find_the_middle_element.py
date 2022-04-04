def gimme(arr: list) -> int:
    return arr.index(sorted(arr)[1])


# Should be 0
arr = [2, 3, 1]

# Should be 2
arr2 = [5, 14, 10]

print(gimme(arr))

print(gimme(arr2))

