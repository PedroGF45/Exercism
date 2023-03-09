def find(list, value):

    copy_search = list.copy()

    # sorting algorithm
    def aux(copy_search, value):
        if value == copy_search[len(copy_search) // 2]:
            return list.index(value)
        elif value > copy_search[len(copy_search) // 2]:
            return aux(copy_search[len(copy_search) // 2 + 1:], value)
        else: 
            return aux(copy_search[:len(copy_search) // 2], value)
    
    # value is not in list
    if value not in copy_search:
        raise ValueError('value not in array')
    else:
        return aux(copy_search, value)
