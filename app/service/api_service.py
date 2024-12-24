import os
from dotenv import load_dotenv
from app.api.news_api import get_new_from_newsapi
import time
from app.kafka_settings.producer import produce



load_dotenv(verbose=True)


news_api_topic = os.getenv('NEWS_API_TOPIC')


def produce_new_from_newsapi_every_two_minutes():
    num = 0
    while True:
        num += 1
        new = get_new_from_newsapi(num)
        produce(news_api_topic, new, 'news')
        time.sleep(12)