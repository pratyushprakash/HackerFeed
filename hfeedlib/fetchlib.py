import json
import requests

from .utils import fetchItem, getArticlesPath
from .parsing.save import savedparser

BASE_URL = 'https://hacker-news.firebaseio.com/v0/'


def getNewArticles(number: int=5,
                   save_flag: bool=False,
                   single: bool=False,
                   start_point: int=0):
    r = requests.get(BASE_URL + 'newstories.json')
    r = json.loads(r.content)
    articles = []

    if single:
        return fetchItem(r[number-1], save_flag=save_flag)

    id_list = r[start_point:start_point+number]
    id_list.reverse()

    for id in id_list:
        articles.append(fetchItem(id, save_flag=save_flag))

    articles.reverse()
    return articles


def getTopArticles(number: int=5,
                   save_flag: bool=False,
                   single: bool=False,
                   start_point: int=0):
    r = requests.get(BASE_URL + 'topstories.json')
    r = json.loads(r.content)
    articles = []

    if single:
        return fetchItem(r[number-1], save_flag=save_flag)

    id_list = r[start_point:start_point+number]
    id_list.reverse()

    for id in id_list:
        articles.append(fetchItem(id, save_flag=save_flag))

    articles.reverse()
    return articles


def getBestArticles(number: int=5,
                    save_flag: bool=False,
                    single: bool=False,
                    start_point: int=0):
    r = requests.get(BASE_URL + 'beststories.json')
    r = json.loads(r.content)
    articles = []

    if single:
        return fetchItem(r[number-1], save_flag=save_flag)

    id_list = r[start_point:start_point+number]
    id_list.reverse()

    for id in id_list:
        articles.append(fetchItem(id, save_flag=save_flag))

    articles.reverse()
    return articles


def getSavedArticles(number: int=5, display_all: bool=False):
    parser = savedparser(getArticlesPath())

    if display_all:
        return parser.parse()

    return parser.parse()[:number]
