def sum_of_multiples(limit, multiples):
    natural = set()
    for multiple in multiples: 
        if multiple == 0:
            continue
        for number in range(1, limit):
            if number % multiple == 0:
                natural.update([number])
    return sum(natural)
