def response(hey_bob):
    hey_bob_cleaned = hey_bob.strip()
    if hey_bob_cleaned.isupper() and hey_bob_cleaned[-1] == '?':
        return 'Calm down, I know what I\'m doing!'
    elif hey_bob_cleaned == "":
        return 'Fine. Be that way!'
    elif hey_bob_cleaned.isupper():
        return 'Whoa, chill out!'
    elif hey_bob_cleaned[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'
