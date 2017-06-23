import sys

from fetchlib import getTopArticles, getBestArticles, getNewArticles
from utils import printArticles, openItem
from cli import hfeedParser


def main():
    p = hfeedParser.parse_args(sys.argv[1:])
    open_item = True if ('open' in dir(p)) else False

    if(p.type == 'top'):

        if(open_item):
            openItem(getTopArticles(p.open)[p.open-1])
        else:
            printArticles(getTopArticles(p.number))

    elif (p.type == 'best'):

        if(open_item):
            openItem(getBestArticles(p.open)[p.open-1])
        else:
            printArticles(getBestArticles(p.number))

    elif (p.type == 'new'):

        if(open_item):
            openItem(getNewArticles(p.open)[p.open-1])
        else:
            printArticles(getNewArticles(p.number))

    elif p.type is None:
        printArticles(getTopArticles(1), show_numbering=False)


if __name__ == '__main__':
    main()
