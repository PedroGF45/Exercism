def flatten(iterable):
    if iterable is None or len(iterable) == 0 :
        return []
    for i in range(len(iterable)):
        if isinstance(iterable[i], int):
            return [iterable[i]] + flatten(iterable[i+1:])
        else:
            return flatten(iterable[i]) + flatten(iterable[i+1:])
        
        