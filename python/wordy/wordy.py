def answer(question):

    question_list = question.replace('?','').split()
    operators = ['plus', 'minus', 'divided by', 'multiplied by']

    if question_list[:2] != ['What', 'is']:
        # if the question is malformed or invalid.
        raise ValueError("syntax error")
    
    if len(question_list) == 3:
        return int(question_list[2])

    if not any(operator in question_list for operator in operators): 
        # if the question contains an unknown operation.
        raise ValueError("unknown operation")

    i = 3
    while i < len(question_list):
        if question_list[i] == 'plus':
            return int(question_list[i - 1]) + int(question_list[i + 1])
        if question_list[i] == 'minus':
            return int(question_list[i - 1]) - int(question_list[i + 1])
        if question_list[i] == 'divided':
            return int(question_list[i - 1]) / int(question_list[i + 1])
        if question_list[i] == 'multiplied':
            return int(question_list[i - 1]) * int(question_list[i + 1])
    
    return 'crl'