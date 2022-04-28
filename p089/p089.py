def romanNumeralParser(romanNumerals: str) -> int:
    """Parses Roman numerals and returns an integer.
    Returns -1 in error condition, where any char inputted is not a Roman numeral."""
    denominations = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    denary = 0
    try:
        prev_char_value = 0
        for char in romanNumerals[:-1].upper():
            current_char_value = denominations[char] 
            if current_char_value < prev_char_value:
                denary -= current_char_value
            elif current_char_value > prev_char_value:
                denary += current_char_value
            else:                                       # this handles the situation where multiple of the same symbol are stacked together
                denary += current_char_value
                prev_char_value += current_char_value

    except KeyError:
        return -1 # error condition
    
    return denary


print(
    romanNumeralParser("XVI"),
    romanNumeralParser("1"),
    romanNumeralParser("abc"),
    romanNumeralParser("xvi")
)
    