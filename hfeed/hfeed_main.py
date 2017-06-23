import sys

from fetchlib import getTopArticles, getBestArticles, getNewArticles
from utils import printArticles, openItem
from cli import hfeedParser


def main():
    p = hfeedParser.parse_args(sys.argv[1:])

    if(p.type == 'top'):

        if(p.id):
            openItem(getTopArticles(p.id)[p.id-1])
        else:
            printArticles(getTopArticles(p.number))

    elif (p.type == 'best'):

        if(p.id):
            openItem(getBestArticles(p.id)[p.id-1])
        else:
            printArticles(getBestArticles(p.number))

    elif (p.type == 'new'):

        if(p.id):
            openItem(getNewArticles(p.id)[p.id-1])
        else:
            printArticles(getNewArticles(p.number))

    elif p.type is None:
        printArticles(getTopArticles(1), show_numbering=False)


if __name__ == '__main__':
    main()
