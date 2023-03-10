def proverb(*words, qualifier=None):
    ans = []

    for index, word in enumerate(words):
        if index == (len(words) - 1) and qualifier is None:
            ans += [f'And all for the want of a {words[0]}.'] 
        elif index == (len(words) - 1) and qualifier is not None:
            ans += [f'And all for the want of a {qualifier} {words[0]}.'] 
        else:
            ans += [f'For want of a {word} the {words[index + 1]} was lost.']
    
    return ans
