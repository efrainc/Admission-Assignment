#!/usr/bin/env python
"""Efrain Camacho Code-Fellows Application - Library Code"""


class book(object):
    """book string"""
    titles = {}

    def __init__(self, *args):
        None
        

    def enshelf(self, title, shelf_number):
        """Places a Book on a Shelf - any number"""

        if self.titles.has_key(title):
            self.titles[title] = shelf_number
        else:
            self.titles.setdefault(title, shelf_number)

    def unshelf(self, title):
        """Removes a Book form the Library and sets it to shelf 0 for tracking"""

        if self.titles.has_key(title):
            self.titles[title] = 0
        else:
            print "%s is not in the Library" %title
            # self.titles.setdefault(title, 'Does Not Exisit')

class shelf(book):
    """Return shelfs and books on each shelf"""

    def __init__(self, *args):
        books_on_shelfs = [[] for x in range(len(set(self.titles.values()))+1)]
        for x in range(len(set(self.titles.values()))+1):
            for k, v in self.titles.iteritems():
                if v == x:
                    books_on_shelfs[x].append(k)
                else:
                    pass
              
        for y in range(len(books_on_shelfs)):
            print "shelf {} has the following books: {}".format(y,books_on_shelfs[y])

                
class library(book):
    """Counts how many shelfs are in the library"""

    def __init__(self, *args):
        total = set(self.titles.values())
        total_shelfs = len(total) - 1
        print "total number of shelfs = %s" %total_shelfs

if __name__ == '__main__':
    test = book()
    a = test.enshelf('book1', 3)
    q = test.enshelf('book1', 2)
    c = test.enshelf('book2', 1)
    d = test.unshelf('book2')
    e = test.unshelf('book3')
    f = library()
    shelfs = shelf()
