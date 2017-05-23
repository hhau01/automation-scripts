#! /usr/bin/python3

# rd.py - rename files with american-style dates to european style dates
# say boss emails you thousands of files with american-style dates(MM-DD-YYYY) in their names
# and needs them renamed to european-style dates(DD-MM-YYYY)

import shutil, os, re

print('American-style dates: "MM-DD-YYYY" to European-style dates: "DD-MM-YYYY"')

# create regex that matches files with an American date format
datePattern = re.compile(r"""^(.*?)     # all text before the date
    ((0|1)?\d)-                         # one or two digits for the month
    ((0|1|2|3)?\d)-                     # one or two digits for the day
    ((19|20)\d\d)                       # four digits for the year
    (.*?)$                              # all text after the date
""", re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths
    # absWorkingDir = os.path.abspath('.')
    # amerFilename = os.path.join(absWorkingDir, amerFilename)
    # euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files
    print('Renaming "{}" to "{}"'.format(amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename) # uncomment after testing