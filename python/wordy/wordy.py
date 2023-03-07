def answer(question):

    question_list = question.replace('?','').replace('by', '').split()
    operators = ['plus', 'minus', 'divided', 'multiplied']

    if len(question_list) < 3:
        # if the question is malformed or invalid.
        raise ValueError("syntax error")

    # if there's no operations return first element
    if question_list[2].lstrip("-").isdigit() and question_list[:2] == ['What', 'is'] and len(question_list) == 3:
        return int(question_list[2])

    if not any(operator in question_list for operator in operators):
        # if the question contains an unknown operation.
        raise ValueError("unknown operation")

    # if thrid element is not digit
    try:
        a = int(question_list[2])
    except:
        raise ValueError("syntax error")
    
    # do calculations
    i = 3
    while i < len(question_list):
        if len(question_list) % 2 == 0 or not question_list[i + 1].lstrip("-").isdigit() or not question_list[i - 1].lstrip("-").isdigit():
            raise ValueError('syntax error')
        if question_list[i] == 'plus':
            a += int(question_list[i + 1])
        if question_list[i] == 'minus':
            a -= int(question_list[i + 1])
        if question_list[i] == 'divided':
            a /= int(question_list[i + 1])
        if question_list[i] == 'multiplied':
            a *= int(question_list[i + 1])
        i += 2
    return a