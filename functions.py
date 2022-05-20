def get_count(number):
    s_number = str(number)
    if '.' in s_number:
        return abs(s_number.find('.') - len(s_number)) - 1
    else:
        return 0


def degree(deg):
    indexes = {"0": "\u2070",
               "1": "\u00B9",
               "2": "\u00B2",
               "3": "\u00B3",
               "4": "\u2074",
               "5": "\u2075",
               "6": "\u2076",
               "7": "\u2077",
               "8": "\u2078",
               "9": "\u2079",
               "-": "\u207B",
               "n": "\u207F",
               ".": "\u0307",
               "+": "\u207A"
               }
    degrees = ""
    temp = str(deg)
    for char in temp:
        degrees += indexes[char] or ""
    return degrees


def downDegree(deg):
    indexes = {"0": "\u2080",
               "1": "\u2081",
               "2": "\u2082",
               "3": "\u2083",
               "4": "\u2084",
               "5": "\u2085",
               "6": "\u2086",
               "7": "\u2087",
               "8": "\u2088",
               "9": "\u2089",
               "-": "\u208B",
               "x": "\u2093",
               ".": "\u0326",
               "+": "\u207A"
               }
    degrees = ""
    temp = str(deg)
    for char in temp:
        degrees += indexes[char] or ""
    return degrees
