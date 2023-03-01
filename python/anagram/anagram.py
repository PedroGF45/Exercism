def find_anagrams(word, candidates):
    res = []
    for candidate in candidates:
        # the sorted strings are checked
        if(sorted(candidate) == sorted(word)):
            res += [candidate]

    return res