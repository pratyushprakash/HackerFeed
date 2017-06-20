import sys
import argparse

from top import getTopArticles
from utils import printArticles

parser = argparse.ArgumentParser(description='Get the latest HackerNews'
                                 'articles right from your command line.')

subparsers = parser.add_subparsers(dest='type', help='sub-commands')

top_parser = subparsers.add_parser('top', help='Get the top'
                                   'articles of HN (default 5)')
top_parser_group = top_parser.add_mutually_exclusive_group()
top_parser_group.add_argument('--number', type=int, default=5,
                              help='Number of articles to'
                              'display (default 5)')
top_parser_group.add_argument('--id', type=int,
                              help='Id of the article to'
                              'be opened')

new_parser = subparsers.add_parser('new', help='Get the new'
                                   'articles of HN (default 5)')
new_parser_group = new_parser.add_mutually_exclusive_group()
new_parser_group.add_argument('--number', type=int, default=5,
                              help='Number of articles to'
                              'display (default 5)')
new_parser_group.add_argument('--id', type=int,
                              help='Id of the article to'
                              'be opened')

best_parser = subparsers.add_parser('best', help='Get the best'
                                    'articles of HN (default 5)')
best_parser_group = best_parser.add_mutually_exclusive_group()
best_parser_group.add_argument('--number', type=int, default=5,
                               help='Number of articles to'
                               'display (default 5)')
best_parser_group.add_argument('--id', type=int,
                               help='Id of the article to'
                               'be opened')


def main():
    p = parser.parse_args(sys.argv[1:])
    if(p.type == 'top'):
        printArticles(getTopArticles(p.number))
        if(p.id):
            print('Id is {}'.format(p.id))
    elif (p.type == 'best'):
        print('Printing the best articles')
        if(p.id):
            print('Id is {}'.format(p.id))

    elif (p.type == 'new'):
        print('Printing the new articles')
        if(p.id):
            print('Id is {}'.format(p.id))


if __name__ == '__main__':
    main()
