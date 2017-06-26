import sys

from fetchlib import (getTopArticles, getBestArticles,
                      getNewArticles, getSavedArticles)
from utils import printArticles, openItem, clearSavedArticles
from parsing.cli import getParser


def main(args=[]):

    hfeedParser = getParser()
    p = hfeedParser.parse_args(args)
    open_item = True if ('open' in dir(p) and p.open is not None) else False
    if(p.type == 'top'):
        if(open_item):
            openItem(getTopArticles(p.open, single=True, save_flag=p.save))
        else:
            printArticles(getTopArticles(p.number, save_flag=p.save))

    elif (p.type == 'best'):

        if(open_item):
            openItem(getBestArticles(p.open, single=True, save_flag=p.save))
        else:
            printArticles(getBestArticles(p.number, save_flag=p.save))

    elif (p.type == 'new'):

        if(open_item):
            openItem(getNewArticles(p.open, single=True, save_flag=p.save))
        else:
            printArticles(getNewArticles(p.number, save_flag=p.save))

    elif (p.type == 'saved'):

        if(open_item):
            openItem(getSavedArticles(p.open)[p.open - 1])
        elif(p.clear):
            clearSavedArticles()
        else:
            printArticles(getSavedArticles(p.number))

    elif p.type is None:
        printArticles([getTopArticles(1, single=True, save_flag=p.save)],
                      show_numbering=False)


if __name__ == '__main__':
    print(sys.argv)
    main(sys.argv[1:])
