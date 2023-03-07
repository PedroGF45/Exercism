verses = [['This is the house that Jack built.'],
        ['This is the malt', 'that lay in the house that Jack built.'],
        ['This is the rat','that ate the malt','that lay in the house that Jack built.'],
        ['This is the cat','that killed the rat','that ate the malt','that lay in the house that Jack built.'],
        ['This is the dog','that worried the cat','that killed the rat','that ate the malt','that lay in the house that Jack built.'],
        ['This is the cow with the crumpled horn','that tossed the dog','that worried the cat','that killed the rat','that ate the malt','that lay in the house that Jack built.'],
        ['This is the maiden all forlorn','that milked the cow with the crumpled horn','that tossed the dog','that worried the cat','that killed the rat','that ate the malt', 'that lay in the house that Jack built.'],
        ['This is the man all tattered and torn','that kissed the maiden all forlorn','that milked the cow with the crumpled horn','that tossed the dog','that worried the cat','that killed the rat','that ate the malt', 'that lay in the house that Jack built.'],
        ['This is the priest all shaven and shorn','that married the man all tattered and torn','that kissed the maiden all forlorn','that milked the cow with the crumpled horn','that tossed the dog','that worried the cat', 'that killed the rat', 'that ate the malt', 'that lay in the house that Jack built.'],
        ['This is the rooster that crowed in the morn','that woke the priest all shaven and shorn','that married the man all tattered and torn','that kissed the maiden all forlorn','that milked the cow with the crumpled horn','that tossed the dog','that worried the cat', 'that killed the rat', 'that ate the malt', 'that lay in the house that Jack built.'],
        ['This is the farmer sowing his corn','that kept the rooster that crowed in the morn','that woke the priest all shaven and shorn','that married the man all tattered and torn','that kissed the maiden all forlorn','that milked the cow with the crumpled horn', 'that tossed the dog', 'that worried the cat', 'that killed the rat', 'that ate the malt', 'that lay in the house that Jack built.'],
        ['This is the horse and the hound and the horn','that belonged to the farmer sowing his corn','that kept the rooster that crowed in the morn','that woke the priest all shaven and shorn','that married the man all tattered and torn','that kissed the maiden all forlorn','that milked the cow with the crumpled horn','that tossed the dog','that worried the cat','that killed the rat','that ate the malt','that lay in the house that Jack built.']]

def recite(start_verse, end_verse):

    def aux(verses):
        ans = ''
        for index, verse in enumerate(verses):
            if index == len(verses) - 1:
                ans += verse
            else:
                ans += verse + ' '
        return [ans]
        
    if start_verse == end_verse:
        return aux(verses[end_verse - 1])
    else:
        return aux(verses[start_verse - 1]) + recite(start_verse + 1, end_verse)
        