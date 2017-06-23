import json
import requests
import webbrowser

from colorama import colorama_text, Fore, Style


BASE_URL = 'https://hacker-news.firebaseio.com/v0/'
YCOMB_URL = 'https://news.ycombinator.com/item?id'


def fetchItem(id: int):
    r = requests.get(BASE_URL + '/item/' + str(id) + '.json')
    r = json.loads(r.content)
    return r


def fetchItems(ids: list):
    articles = []
    for id in ids:
        articles.append(fetchItem(id))

    return articles


def formatItem(item):
    with colorama_text():
        if 'url' in item.keys():
            return str(Fore.YELLOW + '{}: '.format(item['title']) +
                       Fore.RESET + Style.DIM + '{}'.format(item['url']) +
                       Style.RESET_ALL)
        else:
            return str(Fore.YELLOW + '{}: '.format(item['title']) +
                       Fore.RESET + Style.DIM + YCOMB_URL +
                       str(item['id']) + Style.RESET_ALL)


def printArticles(articles: list, show_numbering=True):
    print()
    for x in range(len(articles)):
        if show_numbering:
            print('{}) {}'.format(str(x+1), formatItem(articles[x])))
        else:
            print(formatItem(articles[x]))
        print()


def openItem(item):
    if 'url' in item.keys():
        webbrowser.open(item['url'])
    else:
        webbrowser.open(YCOMB_URL + str(item['id']))
