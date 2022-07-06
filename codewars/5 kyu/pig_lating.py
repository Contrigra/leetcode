def pig_it(text) -> str:
    # text_array = text.split()
    # moved_array = []
    # for i, s in enumerate(text_array):
    #     moved_array.append(s[1::])
    #     if s.isalpha():
    #         moved_array[i] += s[0] + 'ay'
    #     else:
    #         moved_array[i] += s[0]
    #
    # return ' '.join(moved_array)

    text_array = text.split()
    moved_array = []
    for i, s in enumerate(text_array):
        moved_array.append(s[1::])
        moved_array[i] += s[0]

        if s.isalpha():
            moved_array[i] += 'ay'

    return ' '.join(moved_array)



print(pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay')
