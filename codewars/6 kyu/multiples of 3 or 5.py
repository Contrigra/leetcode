def solution(number) -> int:
    if number < 0:
        return 0

    multiples = []
    for i in range(number):
        if i % 3 == 0:
            multiples.append(i)
        elif i % 5 == 0:
            multiples.append(i)

    return sum(multiples)


print(solution(10) == 23)

print(sum([i for i in range(10) if i % 3 == 0 or i % 5 == 0]))