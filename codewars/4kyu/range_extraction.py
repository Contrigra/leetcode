from itertools import groupby
from typing import Iterable


def grouping(arr) -> list[Iterable]:
    grouped_arr = []
    for _, g in groupby(enumerate(arr), lambda x: x[0] - x[1]):
        grouped_arr.append([x[1] for x in g])

    return grouped_arr


def stringify(arr) -> str:
    output_string = ''
    for i in arr:
        if len(i) > 2:
            output_string += f'{i[0]}-{i[-1]},'
        else:
            for j in i:
                output_string += f'{j},'

    return output_string[:-1]


def solution(arr) -> str:
    grouped_arr = grouping(arr)

    valid_string = stringify(grouped_arr)

    return valid_string


arr1 = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19,
        20]
print(solution(
    arr1) == '-6,-3-1,3-5,7-11,14,15,17-20'
      )

print(solution(arr1))

arr2 = [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]
print(solution(arr2) ==
      '-3--1,2,10,15,16,18-20'
      )
