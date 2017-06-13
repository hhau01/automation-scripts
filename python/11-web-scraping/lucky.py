#!/usr/bin/env python3

# Gets search keywords from command line arguments. Retrieves the search results page. Opens a browser tab for each result.

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
# always use raise_for_status to check if webpage has been loaded
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))

for i in range(0,5):
    print(linkElems[i])
    print()

# This will open all 5 tabs in your default webbrowser
# for i in range(numOpen):
    # webbrowser.open('https://google.com' + linkElems[i].get('href'))

