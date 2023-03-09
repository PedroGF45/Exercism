def find(list, value):

    copy_search = list.copy()
    index = len(copy_search) // 2

    # sorting algorithm
    def aux(copy_search, value):
        if value == copy_search[index]:
            return list.index(value)
        elif value > copy_search[index]:
            return aux(copy_search[index + 1:], value)
        else: 
            return aux(copy_search[:index], value)
    
    # value is not in list
    if value not in copy_search:
        raise ValueError('value not in array')
    else:
        return aux(copy_search, value)
