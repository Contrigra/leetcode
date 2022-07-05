def spin_words(sentence) -> str:
    arr = sentence.split(' ')
    for i, v in enumerate(arr):
        if len(v) >= 5:
            arr[i] = v[::-1]
    s = ' '.join(arr)
    return s

a = spin_words("Hey fellow warriors")
print(a)
print(spin_words("Hey fellow warriors") == "Hey wollef sroirraw")


