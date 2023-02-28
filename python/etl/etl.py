def transform(legacy_data):

    # initialize a new dictionary to store the new data system
    new_data = {}

    for score in legacy_data:
        # for each letter in each score
        for letter in legacy_data[score]:
            new_data[letter.lower()] = score

    return new_data
