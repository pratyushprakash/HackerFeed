import sys
import argparse

from fetchlib import getTopArticles, getBestArticles, getNewArticles
from utils import printArticles, openItem


parser = argparse.ArgumentParser(description='Get the latest HackerNews'
                                 'articles right from your command line.')

subparsers = parser.add_subparsers(dest='type', help='sub-commands')

top_parser = subparsers.add_parser('top', help='Get the top'
                                   'articles of HN (default 5)')
top_parser_group = top_parser.add_mutually_exclusive_group()
top_parser_group.add_argument('-n', '--number', type=int, default=5,
                              help='Number of articles to'
                              'display (default 5)')
top_parser_group.add_argument('-o', '--open', type=int,
                              help='Number of the article to'
                              'be opened')

new_parser = subparsers.add_parser('new', help='Get the new'
                                   'articles of HN (default 5)')
new_parser_group = new_parser.add_mutually_exclusive_group()
new_parser_group.add_argument('-n', '--number', type=int, default=5,
                              help='Number of articles to'
                              'display (default 5)')
new_parser_group.add_argument('-o', '--open', type=int,
                              help='Number of the article to'
                              'be opened')

best_parser = subparsers.add_parser('best', help='Get the best'
                                    'articles of HN (default 5)')
best_parser_group = best_parser.add_mutually_exclusive_group()
best_parser_group.add_argument('-n', '--number', type=int, default=5,
                               help='Number of articles to'
                               'display (default 5)')
best_parser_group.add_argument('-o', '--open', type=int,
                               help='Number of the article to'
                               'be opened')


def main():
    p = parser.parse_args(sys.argv[1:])

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
