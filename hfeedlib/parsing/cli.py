import argparse


def getParser():

    hfeedParser = argparse.ArgumentParser(description='Get the latest '
                                          'HackerNews '
                                          'articles right '
                                          'from your command line.')
    hfeedParser.add_argument('-s', '--save', action='store_true',
                             help='Save the articles')

    subparsers = hfeedParser.add_subparsers(dest='type', help='sub-commands')

    # Top Sub-Parser

    top_parser = subparsers.add_parser('top', help='Get the top '
                                       'articles of HN (default 5)')
    top_parser.add_argument('-s', '--save', action='store_true',
                            help='Save the articles')

    top_parser_group = top_parser.add_mutually_exclusive_group()
    top_parser_group.add_argument('-n', '--number', type=int, default=5,
                                  help='Number of articles to '
                                  'display (default 5)')
    top_parser_group.add_argument('-o', '--open', type=int,
                                  help='Number of the article to '
                                  'be opened')

    # New Sub-Parser

    new_parser = subparsers.add_parser('new', help='Get the new '
                                       'articles of HN (default 5)')
    new_parser.add_argument('-s', '--save', action='store_true',
                            help='Save the articles')

    new_parser_group = new_parser.add_mutually_exclusive_group()
    new_parser_group.add_argument('-n', '--number', type=int, default=5,
                                  help='Number of articles to '
                                  'display (default 5)')
    new_parser_group.add_argument('-o', '--open', type=int,
                                  help='Number of the article to '
                                  'be opened')

    # Best Sub-Parser

    best_parser = subparsers.add_parser('best', help='Get the best '
                                        'articles of HN (default 5)')
    best_parser.add_argument('-s', '--save', action='store_true',
                             help='Save the articles')

    best_parser_group = best_parser.add_mutually_exclusive_group()
    best_parser_group.add_argument('-n', '--number', type=int, default=5,
                                   help='Number of articles to '
                                   'display (default 5)')
    best_parser_group.add_argument('-o', '--open', type=int,
                                   help='Number of the article to '
                                   'be opened')

    # Saved Sub-Parser

    saved_parser = subparsers.add_parser('saved', help='List your '
                                         'saved articles')
    saved_parser_group = saved_parser.add_mutually_exclusive_group()

    saved_parser_group.add_argument('-n', '--number', type=int, default=5,
                                    help='Number of articles to '
                                    'display (default 5)')
    saved_parser_group.add_argument('-o', '--open', type=int,
                                    help='Number of the article to '
                                    'be opened')
    saved_parser_group.add_argument('-c', '--clear', action='store_true',
                                    help='Clear your saved articles')
    saved_parser_group.add_argument('-r', '--remove', type=int,
                                    help='Number of the article to be '
                                    'removed')
    saved_parser_group.add_argument('-a', '--all', action='store_true',
                                    help='Display all saved Articles')

    return hfeedParser
