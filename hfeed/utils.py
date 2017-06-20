import json
import requests

from colorama import colorama_text, Fore, Style

BASE_URL = 'https://hacker-news.firebaseio.com/v0/'


def fetchItem(id: int):
    r = requests.get(BASE_URL + '/item/' + str(id) + '.json')
    r = json.loads(r.content)
    return r


def fetchItems(ids: list):
    articles = []
    for id in ids:
        articles.append(fetchItem(id))

    return articles


def printArticle(item):
    if not item['type'] == 'story':
        print('Item not a story!')
    else:
        with colorama_text():
            print(Fore.GREEN + '{}:'.format(item['title']) +
                  Fore.RESET + Style.DIM + ' {}'.format(item['url']) +
                  Style.RESET_ALL)
        print()


def printArticles(articles: list):
    print()
    for article in articles:
        printArticle(article)
