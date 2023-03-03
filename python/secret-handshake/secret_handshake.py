def commands(binary_str):

    # actions with their binnary indeces
    actions = {
        '4': 'wink',
        '3': 'double blink',
        '2': 'close your eyes',
        '1': 'jump'
    }

    # initialize handshake list
    handshake = []

    for bin, act in actions.items():
        if binary_str[int(bin)] == '1':
            handshake += [act]

    # if first element is 1 then reverse the actions in handshake
    if binary_str[0] == '1':
        handshake.reverse()
        return handshake
    else:
        return handshake
