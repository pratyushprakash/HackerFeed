import json
import requests

from utils import fetchItem


BASE_URL = 'https://hacker-news.firebaseio.com/v0/'


def getNewArticles(number: int=5):
    r = requests.get(BASE_URL + 'newstories.json')
    r = json.loads(r.content)
    articles = []
    for id in r[:number]:
        articles.append(fetchItem(id))
    return articles


def getTopArticles(number: int=5):
    r = requests.get(BASE_URL + 'topstories.json')
    r = json.loads(r.content)
    articles = []
    for id in r[:number]:
        articles.append(fetchItem(id))
    return articles


def getBestArticles(number: int=5):
    r = requests.get(BASE_URL + 'beststories.json')
    r = json.loads(r.content)
    articles = []
    for id in r[:number]:
        articles.append(fetchItem(id))
    return articles
