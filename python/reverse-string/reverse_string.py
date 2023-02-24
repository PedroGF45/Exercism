def reverse(text):
    i = 0
    new_text = ''
    while i < len(text):
        new_text += text[len(text) - 1 - i]
        i += 1
    return new_text
