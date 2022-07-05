def disemvowel(string_):
    vowels = 'aeiuoAEIUO'
    new_string = ''
    for c in string_:
        if c not in vowels:
            new_string += c

    return new_string


print(disemvowel('This website is for losers LOL'))