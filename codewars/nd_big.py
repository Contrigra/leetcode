import functools
import timeit

def nb_dig(n, d):
    d = str(d)
    count = 0
    for k in range(n + 1):
        k = k ** 2
        k = str(k)
        for s in k:
            if s == d:
                count += 1
    return count


def nb_dig2(n, d):
    return sum(str(i * i).count(str(d)) for i in range(n + 1))


print(timeit.Timer(functools.partial(nb_dig, 5750, 0)).timeit(500))
print(timeit.Timer(functools.partial(nb_dig2, 5750, 0)).timeit(500))

