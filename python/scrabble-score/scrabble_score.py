def score(word):

    letter_value = {
        'aeioulnrst': 1,
        'dg': 2,
        'bcmp': 3,
        'fhvwy': 4,
        'k': 5,
        'jx': 8,
        'qz': 10
    }

    score = 0

    for letter_word in word:
        for letter, value in letter_value.items():
            if letter_word.lower() in letter:
                score += value

    return score