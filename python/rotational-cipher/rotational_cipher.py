def rotate(text, key):

    # Define letters
    letters = 'abcdefghijklmnopqrstuvwxyz'

    def check_index(index, key):
        if index + key < 26:
            return index + key
        else:
            return index + key - 26

    ans = ''

    for text_letter in text:
        print(text_letter)
        if text_letter.isalpha() and text_letter.isupper():
            ans += letters[check_index(letters.rindex(text_letter.lower()), key)].upper()
        elif text_letter.isalpha() and text_letter.islower():
            ans += letters[check_index(letters.rindex(text_letter), key)]
        else:
            ans += text_letter

    return ans
