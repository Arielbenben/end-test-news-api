import os
import requests
from dotenv import load_dotenv


load_dotenv(verbose=True)


news_api = os.getenv('NEWSAPI_KEY')


def get_params_for_newsapi(count: int):
    return {
        "action": "getArticles",
        "keyword": "terror attack",
        "ignoreSourceGroupUri": "paywall/paywalled_sources",
        "articlesPage": count,
        "articlesCount": 100,
        "articlesSortBy": "socialScore",
        "articlesSortByAsc": False,
        "dataType": [
            "news",
            "pr"
        ],
        "forceMaxDataTimeWindow": 31,
        "resultType": "articles",
        "apiKey": news_api
    }


def get_new_from_newsapi(count: int):
    url = 'https://eventregistry.org/api/v1/article/getArticles'
    body = get_params_for_newsapi(count)
    response = requests.post(url, json=body)

    if response.status_code == 200:
        response = response.json()['articles']['results'][0]
        return response
    else:
        raise Exception(f"API Error: {response.status_code}")





