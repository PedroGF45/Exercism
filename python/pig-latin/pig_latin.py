def translate(text):
    vowels = 'aeiou'

    def translate_word(text_f):         
        if text_f[0:2] in ['xr', 'yt'] or text_f[0] in vowels:
            return text_f + 'ay'
        else:
            for i in range(1, len(text_f)):
                if text_f[i] in vowels or (text_f[i] == 'y' and i != 1):
                    if text_f[i-1:i+1] != 'qu':
                        # Rule 2: If text_f starts with a consonant cluster or "y", move it to the end and add "ay"
                        return text_f[i:] + text_f[:i] + 'ay'
                    else:
                        # Rule 3: If text_f starts with consonant sound followed by "qu", move it to the end and add "ay"
                        return text_f[i+1:] + text_f[:i+1] + 'ay'
                
            return text_f[i:] + text_f[:i] + 'ay'
        
    if ' ' in text:
        ans = []
        words = text.split()
        print(words)
        for word in words:
            print( word)
            ans += [translate_word(word)]
        return ' '.join(ans)
    else:
        return translate_word(text)