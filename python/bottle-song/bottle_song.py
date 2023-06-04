NUMBERS = ["no",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten"]

FIRST_LYRICS = "hanging on the wall,"

SECOND_LYRICS = "And if one green bottle should accidentally fall,"
 
FOURTH_LYRICS = "There'll be "

LAST_LYRICS = "hanging on the wall."

def recite(start, take=1):
    
    res = []

    end = start - take

    while (start > end):
        if start > 1:
            res += [NUMBERS[start] + " green bottles " + FIRST_LYRICS] * 2
        else:
            res += [NUMBERS[start] + " green bottle " + FIRST_LYRICS] * 2

        res += [SECOND_LYRICS]

        if ((start - 1) == 1):
            res += [FOURTH_LYRICS + NUMBERS[start - 1].lower() + " green bottle " + LAST_LYRICS]
        else:
            res += [FOURTH_LYRICS + NUMBERS[start - 1].lower() + " green bottles " + LAST_LYRICS]

        start -= 1

        if start != end:
            res += [""]

    return res
