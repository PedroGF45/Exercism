FIRST_VERSE = "I know an old lady who swallowed a"
FINAL_VERSE = "I don\'t know why she swallowed the fly. Perhaps she\'ll die."
END_VERSE = "She's dead, of course!"
ANIMALS = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
ANIMALS_VERSE = ["It wriggled and jiggled and tickled inside her.",
                    "How absurd to swallow a bird!",
                    "Imagine that, to swallow a cat!",
                    "What a hog, to swallow a dog!",
                    "Just opened her throat and swallowed a goat!",
                    "I don't know how she swallowed a cow!"]
OPTIONAL_BIRD_SPIDER = "that wriggled and jiggled and tickled inside her."
SWALLOW_VERSE = ["She swallowed the", "to catch the"]

def recite(start_verse, end_verse):

    music = []
    
    for verse_index in range(start_verse, end_verse + 1):

        music.append(f"{FIRST_VERSE} {ANIMALS[verse_index - 1]}.")

        if 1 < verse_index < 8:
            music.append(ANIMALS_VERSE[verse_index - 2])

        if verse_index != 8:
            for descendent_index in range(verse_index, 0, -1):
                if descendent_index > 1:
                    swallowed_animal = ANIMALS[descendent_index - 1]
                    to_catch_animal = ANIMALS[descendent_index - 2]
                    if descendent_index == 3:
                        if end_verse == 2:
                            music.append(f"{SWALLOW_VERSE[0]} {swallowed_animal} {SWALLOW_VERSE[1]} {to_catch_animal}.")
                        else:
                            music.append(f"{SWALLOW_VERSE[0]} {swallowed_animal} {SWALLOW_VERSE[1]} {to_catch_animal} {OPTIONAL_BIRD_SPIDER}")
                    else:
                        music.append(f"{SWALLOW_VERSE[0]} {swallowed_animal} {SWALLOW_VERSE[1]} {to_catch_animal}.")
            music.append(FINAL_VERSE)
        else:
            music.append(END_VERSE)

        if verse_index != end_verse:
            music.append("")

    return music
