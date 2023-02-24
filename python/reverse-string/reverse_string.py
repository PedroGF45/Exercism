def reverse(text):
    i = 0
    new_text = ''
    while i < len(text):
        new_text += text[len(text) - 1 - i]
        i += 1
    return new_text

def reverse_option(text):
    a = list((map(lambda x: text[-x -1], range(len(text)))))
    new_text = ''
    for item in a:
        new_text += item
    return new_text

def reverse_option_option(text):
    return text[::-1]
    