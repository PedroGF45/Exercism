def slices(series, length):
    
    #unsupported values
    if series == '':
        raise ValueError("series cannot be empty")
    elif length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    elif length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    
    return [series[i:i+length] for i in range(0, len(series) - length + 1)]
