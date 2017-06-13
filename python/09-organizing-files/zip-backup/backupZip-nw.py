#! /usr/bin/python3

# backupZip.py - Copies entire folder and its contents into a ZIP file

import zipfile, os

path = os.getcwd()
print(path)

def backupZip(folder):
    # backup the entire contents of "folder" into ZIP file
    folder = os.path.abspath(folder) # make sure folder is absolute
    print(folder)

    # figure out the filename this code should use based on what file already exists
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        print(zipFilename)
        print(os.path.exists(zipFilename))
        if not os.path.exists(zipFilename):
            break
        number += 1

        # create ZIP file
        print('Creating {}...'.format(zipFilename))
        backupZip = zipfile.ZipFile(zipFilename, 'w')

        # walk the entire folder tree and compress the files in each folder
        for foldername, subfolders, filenames in os.walk(folder):
            print('Adding files in {}...'.format(foldername))
            # adding current folder to the ZIP file
            backupZip.write(foldername)
            # add all the files in this folder to the ZIP file
            for filename in filenames:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue # dont back up the backup ZIP files
                backupZip.write(os.path.join(foldername, filename))
            backupZip.close()
            print('Done.')

backupZip(path)
