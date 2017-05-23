#! python

# mcb.py - multiclipboard: saves and loads pieces of text to the clipboard.
# usage: py mcb.py save <keyword> - saves clipboard to keyword
#        py mcb.py del <keyword> - deletes keyword from list  
#        py mcb.py <keyword> - loads keyword to clipboard
#        py mcb.py list - loads all keywords to clipboard and prints all keys and values

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        # print(list(mcbShelf.items()))
        for k,v in mcbShelf.items():
            print({k: v})
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
else:
    print('''\tmcb.py - Multiclipboard: saves and loads pieces of text to the clipboard.
    
        Usage: py mcb.py save <keyword> - saves clipboard to keyword 
               py mcb.py del <keyword> - deletes keyword from list
               py mcb.py <keyword> - loads keyword to clipboard
               py mcb.py list - loads all keywords to clipboard and prints all keys and values
    ''')
mcbShelf.close()

