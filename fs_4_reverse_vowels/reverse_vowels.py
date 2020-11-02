def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    holding = []
    for i in s:
        if i in vowels:
            holding.append(i)

    # print(holding)
    new_string = ''
    idx = 0
    for i in s:
        if i in vowels:
            new_string += holding.pop()
            idx += 1
        else:
            new_string += i



    return new_string