def find_anagrams(word, candidates):
    res = []
    for candidate in candidates:
        # the sorted strings are checked
        if(sorted(candidate.lower()) == sorted(word.lower())) and candidate.lower() != word.lower():
            res += [candidate]

    return res