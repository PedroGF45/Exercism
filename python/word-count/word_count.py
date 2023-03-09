import string

def count_words(sentence):
    split_words = sentence.strip("'").replace('\t', ' ').replace('\n', ' ').translate(str.maketrans(string.punctuation.replace("'", ''), ' '*len(string.punctuation.replace("'", '')))).lower().split()
    cleaned_sentence = [word.strip("'") for word in split_words]
    ans = {}
    for word in set(cleaned_sentence):
        ans[word] = cleaned_sentence.count(word)
    return ans
