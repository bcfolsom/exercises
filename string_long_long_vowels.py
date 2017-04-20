long_vowels = ('oo', 'ooooo'), ('ee', 'eeeee')
paragraph = "He drew a doodle of poodle eating noodles and cheese."

new_paragraph = paragraph
for old, new in long_vowels:
    new_paragraph = new_paragraph.replace(old, new)

print (new_paragraph)
