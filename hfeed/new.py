import json
import requests

from utils import fetchItem, printArticles


BASE_URL = 'https://hacker-news.firebaseio.com/v0/'


def getNewArticles(number: int=5):
    r = requests.get(BASE_URL + 'newstories.json')
    r = json.loads(r.content)
    articles = []
    for id in r[:number]:
        articles.append(fetchItem(id))
    return articles


if __name__ == '__main__':
    items = getNewArticles()
    printArticles(items)
