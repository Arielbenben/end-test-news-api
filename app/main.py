from app.kafka_settings.init_topics import init_topics
from app.service.api_service import produce_new_from_newsapi_every_two_minutes





if __name__ == '__main__':
    init_topics()
    produce_new_from_newsapi_every_two_minutes()