#! python

# bpAdder - adds wikipedia bullet points to the start of each line of text on the clipboard
# to use: simply copy this test list
# Lists of animals
# Lists of aquarium life
# Lists of biologists by author abbreviation
# Lists of cultivars

# and then type: py bpAdder.py
# and then paste anywhere!

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add start to each string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text)
