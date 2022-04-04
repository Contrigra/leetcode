arr = [30, 90, 100, 20, 80, 50, 40]

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i, value in enumerate(arr):
        if value < smallest:
            smallest = value
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    sorted_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


arr = selection_sort(arr)

print(arr)