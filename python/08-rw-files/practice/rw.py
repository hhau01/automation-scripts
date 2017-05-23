#! python

import pprint
import shelve
import os

path = 'D:\\++Code\\automation\\python\\06-manipulating-strings\\tablePrinter.py'

print(os.listdir(os.getcwd()))
# print(os.listdir(os.path.abspath('.\\06-manipulating-strings')))
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))

print(os.path.getsize(path))

# get total size of 'thispath' in bytes
thispath = 'D:\\++Code\\automation\\python\\06-manipulating-strings'
totalsize = 0
for file in os.listdir(thispath):
    totalsize = totalsize + os.path.getsize(os.path.join(thispath, file))
print(totalsize)

print(os.path.exists(path))
print(os.path.exists(thispath))
print(os.path.isdir(path))
print(os.path.isdir(thispath))
print(os.path.isfile(path))
print(os.path.isfile(thispath))

wikifile = open('test.txt')
wikiread = wikifile.read()
# print(wikiread)
wikifile.close()

print()

sonnet = open('sonnet29.txt').read().replace('\n', ' ')
# print(sonnet)
# sonnet.close()

baconfile = open('bacon.txt', 'w')
baconfile.write('Hello world!\n')
baconfile.close()

baconfile = open('bacon.txt', 'a')
baconfile.write('Bacon is not a vegetable.\n')
baconfile.close()

baconfile = open('bacon.txt')
print(baconfile.read())
baconfile.close()

# shelve saves data to a binary file
shelffile = shelve.open('mydata')
cats = ['Sophie', 'Pooky', 'Simone']
shelffile['cats'] = cats
shelffile.close()

shelffile = shelve.open('mydata')
print(list(shelffile.items()))
print(shelffile['cats'])
shelffile.close()

dogs = [{'name': 'Zephyr', 'desc': 'chubby'}, {'name': 'Booger', 'desc': 'fluffy'}]
# pprint.pformat(dogs)
fileobj = open('mydogs.py', 'w')
fileobj.write('dogs = ' + pprint.pformat(dogs) + '\n')
fileobj.close()

import mydogs
yodogs = mydogs.dogs
print(yodogs)