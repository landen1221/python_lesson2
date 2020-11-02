def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    return ''.join([phrase[i] for i in range(len(phrase)-1,-1,-1)])

print(reverse_string('happy'))