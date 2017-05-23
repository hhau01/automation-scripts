import shutil, os

# os.chdir('..\\')
shutil.copy('.\\test.txt', '.\\test2.txt')
shutil.copytree('.\\practice', '.\\practice2')
shutil.move('.\\test.txt', '.\\test3.txt')

path = '.\\test3.txt'
os.unlink(path) # delete file at path
os.rmdir(path) # works the same as rmdir in linux
shutil.rmtree(path) # rm -rf

for file in os.listdir():
    if file.endswith('.txt'):
        # os.unlink(file)
        print(file)

# send2trash is safe because instead of permanently deleting the file, it sends it to the trash
import send2trash
baconFile = open('bacon.txt', 'a')
baconFile.write('Baconnnnnnnnnn')
baconFile.close()
send2trash.send2trash('bacon.txt')

# walking a directory tree
"""
    os.walk() function is passed a single string value: the path of a folder

    returns: 
            1. a string of the current folder's name
            2. a list of strings of the folders in the current folder
            3. a list of strings of the files in the current folder
"""

for foldername, subfolders, filenames in os.walk(os.getcwd()):
    print('The current folder is ' + foldername)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + foldername + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + foldername + ': ' + filename)

    print()

# reading zip files
import zipfile
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist() # print?
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
spamInfo.compress_size
print('Compressed file is {}x smaller!'.format(round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()

# extracting from zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()

# extract only select files
exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', os.getcwd())
exampleZip.close()

# creating and adding to zip files
newZip = zipfile.ZipFile('new.zip', 'a')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
