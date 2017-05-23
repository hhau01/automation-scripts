#! python

# tablePrinter.py - takes list of lists of strings and displays it in a well organized table

def printTable(table):
    colWidths = list(map(lambda x: len(max(x)), table)) # grab length of longest string per column
    colWidth = max(colWidths) + 1
    for i in range(len(table[0])):
        for j in range(len(table)):
            word = table[j][i].rjust(colWidth)
            print(word, end='')
        print()

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)