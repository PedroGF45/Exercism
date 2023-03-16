def recite(start_verse, end_verse):
    
    days = [
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
        'eleventh',
        'twelfth'
    ]

    verses = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ",
    ]

    beginning_verse = f"On the {days[start_verse - 1]} day of Christmas my true love gave to me: "

    def aux(start_verse):
        if start_verse == 1:
            return verses[0]
        else:
            return ''.join(verses[i] for i in range(start_verse-1,0,-1)) + 'and ' + verses[0]

    if start_verse == end_verse:
        return [beginning_verse + aux(start_verse)]
    elif start_verse < end_verse:
        return [beginning_verse + aux(start_verse)] + recite(start_verse + 1, end_verse)
