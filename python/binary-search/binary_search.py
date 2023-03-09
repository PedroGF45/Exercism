def find(list, value):

    # value is not in list
    if value not in list:
        raise ValueError('value not in array')

    index = len(list) // 2

    if value == list[index]:
        return index
    elif value > list[index]:
        return find(list[index + 1:], value) + index + 1
    else: 
         return find(list[:index], value)
    