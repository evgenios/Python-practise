class OutOfRangeError(ValueError):
    pass


class NotIntegerError(ValueError):
    pass


def from_roman(string):
    """convert Roman numeral to integer"""
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while string[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


def to_roman(number):
    '''convert integer to Roman numeral'''
    if not (0 < number < 4000):
        raise OutOfRangeError
    if not isinstance(number, int):
        raise NotIntegerError

    result = ''
    for numeral, integer in roman_numeral_map:
        while number >= integer:
            result += numeral
            number -= integer
    return result


roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))
