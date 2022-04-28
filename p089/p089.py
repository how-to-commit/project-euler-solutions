def romanNumeralParser(inp: str) -> int:
    """Parses Roman numerals and returns an integer."""
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
    for i in range(len(inp)):
        casefold_inp = inp.upper()
        try:
            value = denominations[casefold_inp[i]]
            # if the value of the next char is bigger than this one, then this char has negative value
            if i+1 < len(inp) and denominations[casefold_inp[i+1]] > value:
                denary -= value
            else:
                denary += value

        # KeyError only raised by Python when casefold_inp[i] is not a valid key in denominations
        except KeyError:
            return ValueError('Input %s is not a valid Roman numeral.' % inp)
    
    return denary


if __name__ == "__main__":
    with open("p089_roman.txt") as ROMAN:
        for line in ROMAN:
            line = line[:-1] # remove the newline at the end
            print(line, romanNumeralParser(line))
    
