def encode(message, rails):
    
    message = message.replace(" ", "")

    grid_dict = _create_encoded_grid(message, rails)

    encoded_message = _create_encoded_message(grid_dict, rails)

    return encoded_message

def _create_encoded_grid(message, rails):

    incrementing_row = True
    row_counter = 0
    grid_dict = {}

    for i in range(rails):
        grid_dict[i] = []

    for letter in message:

        grid_dict[row_counter].append(letter)

        if incrementing_row:
            row_counter += 1

            if row_counter >= rails - 1:
                incrementing_row = False
        else: 
            row_counter -= 1

            if row_counter <= 0:
                incrementing_row = True

    return grid_dict

def _create_encoded_message(grid_dict, rails):

    message = ''

    for i in range(rails):
        message += ''.join(grid_dict[i])

    return message

def decode(encoded_message, rails):
    
    grid_dict = _create_decoded_grid(encoded_message, rails)

    decoded_message = _create_decoded_message(encoded_message, grid_dict, rails)

    return decoded_message


def _create_decoded_grid(message, rails):

    incrementing_row = True
    row_counter = 0
    grid_dict = {}
    row_dict = {}

    for i in range(rails):
        grid_dict[i] = 0

    for _ in message:

        grid_dict[row_counter] += 1

        if incrementing_row:
            row_counter += 1

            if row_counter >= rails - 1:
                incrementing_row = False
        else: 
            row_counter -= 1

            if row_counter <= 0:
                incrementing_row = True

    for i in range(rails):
        if i == 0:
            row_dict[i] = list(message[:grid_dict[i]])
        elif i == rails - 1:
            row_dict[i] = list(message[-grid_dict[i]:])
        else:
            start_index = 0
            for j in range(i):
                start_index += grid_dict[j]

            row_dict[i] = list(message[start_index:start_index + grid_dict[i]])

    return row_dict

def _create_decoded_message(encoded_message, grid_dict, rails):

    incrementing_row = True
    row_counter = 0
    decoded_message = ''

    for _ in encoded_message:
        
        decoded_message += grid_dict[row_counter].pop(0)

        if incrementing_row:
            row_counter += 1

            if row_counter >= rails - 1:
                incrementing_row = False
        else: 
            row_counter -= 1

            if row_counter <= 0:
                incrementing_row = True

    return decoded_message
        